import string

from langchain_core.messages import AIMessage, AnyMessage, HumanMessage, SystemMessage

from app.core.agent.state import TherapySession
from app.schemas import Score


def replace_template(template, metadata):
    formatter = string.Formatter()
    fields = [
        field_name
        for _, field_name, _, _ in formatter.parse(template)
        if field_name is not None
    ]

    result = template
    for field in fields:
        if field in metadata:
            result = result.replace(f"{{{field}}}", str(metadata[field]))
        else:
            result = result.replace(f"{{{field}}}", "")

    return result


def create_messages(
    chat_prompt: list[tuple[str, str]],
    metadata: dict[str, str],
) -> list[AnyMessage]:
    messages = []
    for role, template in chat_prompt:
        content = replace_template(template, metadata)
        match role:
            case "system":
                messages.append(SystemMessage(content=content))
            case "user":
                messages.append(HumanMessage(content=content))
            case "assistant":
                messages.append(AIMessage(content=content))
            case _:
                raise ValueError(f"Invalid role: {role}")
    return messages


def group_scores(therapy_sessions: list[TherapySession], scores: list[Score]):
    for therapy_session in therapy_sessions:
        therapy_session["scores"] = [
            score for score in scores if score.session_id == therapy_session["id"]
        ]
    return therapy_sessions


def create_human_therapy_assessment(therapy_sessions: list[TherapySession]) -> str:
    if not therapy_sessions:
        return ""

    result = ""
    for therapy_session in therapy_sessions:
        if not therapy_session:
            continue

        result += f"## Session {therapy_session['timestamp']}\n\n"
        scores = therapy_session["scores"]
        if not scores:
            continue

        for score in scores:
            if score:
                result += f"### Score: {score.score_name}\n"
                result += f"Reason: {score.reason}\n"
                result += f"Value: {score.score}\n"

    return result
