from typing import Literal

from pydantic import BaseModel, Field


class LLMScore(BaseModel):
    reason: str = Field(
        ...,
        description="The detailed thinking process that led to the score.",
    )
    score: int = Field(
        ...,
        description="The score assigned to the session, ranging from 1 to 10.",
    )


class Score(LLMScore):
    session_id: int = Field(
        ...,
        description="The unique identifier of the therapy session.",
    )
    score_name: str = Field(
        ...,
        description="The name of the score.",
    )


class TherapyProgressAssessment(BaseModel):
    reason: str = Field(
        ...,
        description="The short reasoning behind the overall therapy progress assessment.",
    )
    progress: Literal[
        "Significantly Worse",
        "Worse",
        "Mildly Worse",
        "Stable",
        "Mildly Better",
        "Better",
        "Significantly Better",
    ] = Field(
        ...,
        description="The overall therapy progress assessment.",
    )
