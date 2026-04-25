import sys
import types
import importlib


def setup_fake_langgraph():
    mod = types.ModuleType("langgraph.graph")

    class StateGraph:
        def __init__(self, _):
            self._nodes = {}
            self._entry = None
            self._edges = {}

        def add_node(self, name, func):
            self._nodes[name] = func

        def set_entry_point(self, name):
            self._entry = name

        def add_edge(self, a, b):
            self._edges.setdefault(a, []).append(b)

        def compile(self):
            nodes = self._nodes.copy()
            entry = self._entry

            class Compiled:
                def invoke(self, state):
                    cur = entry
                    st = state.copy()
                    # simple linear traversal memory->search->llm
                    order = ["memory", "search", "llm"]
                    for n in order:
                        fn = nodes.get(n)
                        if fn:
                            res = fn(st)
                            if isinstance(res, dict):
                                st.update(res)
                    return st

            return Compiled()

    mod.StateGraph = StateGraph
    mod.END = object()
    sys.modules["langgraph.graph"] = mod


def setup_fake_nodes():
    # memory node
    mem = types.ModuleType("app.graphs.nodes.memory_node")

    def memory_node(state):
        return {**state, "memory": ["m1"]}

    mem.memory_node = memory_node
    sys.modules["app.graphs.nodes.memory_node"] = mem

    # search node
    s = types.ModuleType("app.graphs.nodes.search_node")

    def search_node(state):
        return {**state, "web_results": ["r1"]}

    s.search_node = search_node
    sys.modules["app.graphs.nodes.search_node"] = s

    # llm node
    l = types.ModuleType("app.graphs.nodes.llm_node")

    def llm_node(state):
        return {"answer": "ok"}

    l.llm_node = llm_node
    sys.modules["app.graphs.nodes.llm_node"] = l


def test_build_and_run_graph_caching(monkeypatch):
    setup_fake_langgraph()
    setup_fake_nodes()

    import app.graphs.qa_graph as gmod
    importlib.reload(gmod)

    g1 = gmod.build_graph()
    g2 = gmod.build_graph()
    assert g1 is g2

    res = gmod.run_graph("123", "hello")
    assert res.get("answer") == "ok"
