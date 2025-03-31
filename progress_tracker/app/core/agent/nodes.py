from typing import cast

from langchain_core.utils import convert_to_secret_str
from langchain_openai import ChatOpenAI
from langfuse import Langfuse
from langgraph.types import Send

from app.core.agent.state import OverallState, ScoreState
from app.core.agent.utils import (
    create_human_therapy_assessment,
    create_messages,
    group_scores,
)
from app.core.settings import get_settings
from app.schemas import LLMScore, Score, TherapyProgressAssessment

settings = get_settings()


async def process_sessions(state: OverallState):
    return [
        Send(
            "generate_score",
            {
                "therapy_session_id": session["id"],
                "therapy_session_summary": session["summary"],
                "score_metric": metric,
            },
        )
        for session in state.get("therapy_sessions", [])
        for metric in settings.THERAPY_METRICS
    ]


async def generate_score(state: ScoreState) -> OverallState:
    langfuse = Langfuse(
        host=settings.LANGFUSE_HOST,
        public_key=settings.LANGFUSE_PUBLIC_KEY,
        secret_key=settings.LANGFUSE_SECRET_KEY,
    )

    generate_score_prompts = cast(
        list[tuple[str, str]],
        langfuse.get_prompt(state["score_metric"]).get_langchain_prompt(),
    )

    messages = create_messages(
        generate_score_prompts,
        {"session_summary": state["therapy_session_summary"].to_human()},
    )

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.0,
        api_key=convert_to_secret_str(settings.OPENAI_API_KEY),
    )

    score_response = await llm.ainvoke(messages)

    extract_score_prompts = cast(
        list[tuple[str, str]],
        langfuse.get_prompt("score-extractor").get_langchain_prompt(),
    )
    messages = create_messages(
        extract_score_prompts,
        {"score": str(score_response.content)},
    )

    structured_llm = llm.with_structured_output(LLMScore)

    llm_score = cast(LLMScore, await structured_llm.ainvoke(messages))
    score = Score(
        **llm_score.model_dump(),
        session_id=state["therapy_session_id"],
        score_name=state["score_metric"],
    )
    return {
        "scores": [score],
    }


async def compare_progress(state: OverallState) -> OverallState:
    langfuse = Langfuse(
        host=settings.LANGFUSE_HOST,
        public_key=settings.LANGFUSE_PUBLIC_KEY,
        secret_key=settings.LANGFUSE_SECRET_KEY,
    )

    therapy_sessions = group_scores(
        state.get("therapy_sessions", []),
        state.get("scores", []),
    )

    therapy_sessions = sorted(therapy_sessions, key=lambda x: x["timestamp"])

    therapy_sessions_str = create_human_therapy_assessment(therapy_sessions)

    compare_progress_prompts = cast(
        list[tuple[str, str]],
        langfuse.get_prompt("compare-progress").get_langchain_prompt(),
    )

    messages = create_messages(
        compare_progress_prompts,
        {"therapy_sessions": therapy_sessions_str},
    )

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.0,
        api_key=convert_to_secret_str(settings.OPENAI_API_KEY),
    )

    structured_llm = llm.with_structured_output(TherapyProgressAssessment)

    llm_progress_assessment = cast(
        TherapyProgressAssessment,
        await structured_llm.ainvoke(messages),
    )

    return {
        "progress_assessment": llm_progress_assessment.progress,
        "progress_assessment_reason": llm_progress_assessment.reason,
    }
