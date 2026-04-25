from langgraph.graph import StateGraph, END

from app.graphs.state import QAState
from app.graphs.nodes.memory_node import memory_node
from app.graphs.nodes.search_node import search_node
from app.graphs.nodes.llm_node import llm_node


# Cache compiled graph to avoid recompiling on every request
_compiled_graph = None


def build_graph():
    global _compiled_graph
    if _compiled_graph is not None:
        return _compiled_graph

    graph = StateGraph(QAState)

    graph.add_node("memory", memory_node)
    graph.add_node("search", search_node)
    graph.add_node("llm", llm_node)

    graph.set_entry_point("memory")
    graph.add_edge("memory", "search")
    graph.add_edge("search", "llm")
    graph.add_edge("llm", END)

    _compiled_graph = graph.compile()
    return _compiled_graph

def run_graph(user_id: str, question: str):
    graph = build_graph()

    result = graph.invoke({
        "user_id": user_id,
        "question": question,
        "memory": [],
        "web_results": [],
        "answer": None
    })

    return result