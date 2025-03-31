from langfuse.callback import CallbackHandler
from langgraph.graph.state import END, START, CompiledStateGraph, StateGraph

from app.core.agent.nodes import compare_progress, generate_score, process_sessions
from app.core.agent.state import OverallState
from app.core.settings import get_settings

settings = get_settings()


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Agent(metaclass=SingletonMeta):
    def __init__(self):
        self.agent = self.create_agent()
        self.callback = CallbackHandler(
            host=settings.LANGFUSE_HOST,
            public_key=settings.LANGFUSE_PUBLIC_KEY,
            secret_key=settings.LANGFUSE_SECRET_KEY,
        )

    def create_agent(self) -> CompiledStateGraph:
        builder = StateGraph(OverallState)
        builder.add_node("generate_score", generate_score)
        builder.add_node("compare_progress", compare_progress)
        builder.add_conditional_edges(START, process_sessions, ["generate_score"])
        builder.add_edge("generate_score", "compare_progress")
        builder.add_edge("compare_progress", END)

        return builder.compile()

    async def compare_sessions(self, state: OverallState):
        return await self.agent.ainvoke(
            state,
            config={"callbacks": [self.callback]},
        )
