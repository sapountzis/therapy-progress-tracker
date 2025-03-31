import operator
from datetime import datetime
from typing import Annotated, TypedDict

from app.schemas import Score, TherapySessionSummary


class TherapySession(TypedDict):
    summary: TherapySessionSummary
    id: int
    timestamp: datetime
    scores: list[Score] | None


class OverallState(TypedDict, total=False):
    therapy_sessions: list[TherapySession]
    scores: Annotated[list[Score], operator.add]
    progress_assessment: str
    progress_assessment_reason: str


class ScoreState(TypedDict):
    therapy_session_id: int
    therapy_session_summary: TherapySessionSummary
    score_metric: str
