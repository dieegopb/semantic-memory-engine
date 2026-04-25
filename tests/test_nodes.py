import sys
import types


def test_memory_node():
    from app.graphs.nodes.memory_node import memory_node

    state = {"user_id": "123"}
    out = memory_node(state)
    assert "memory" in out
    assert isinstance(out["memory"], list)


def test_search_node(monkeypatch):
    from app.graphs.nodes import search_node
    from app.services.search_service import SearchService

    monkeypatch.setattr(SearchService, "search", lambda self, q: ["s1"])

    out = search_node.search_node({"question": "q"})
    assert out["web_results"] == ["s1"]


def test_llm_node_with_fake_client(monkeypatch):
    # inject fake module before importing llm_node
    fake_mod = types.ModuleType("app.llm.client")
    fake_mod.generate_response = lambda prompt: "FAKE_ANSWER"
    sys.modules["app.llm.client"] = fake_mod

    # reload the llm_node module to pick up the fake client
    import importlib
    import app.graphs.nodes.llm_node as llm_mod
    importlib.reload(llm_mod)

    out = llm_mod.llm_node({"question": "q", "memory": [], "web_results": ["w"]})
    assert out["answer"] == "FAKE_ANSWER"
