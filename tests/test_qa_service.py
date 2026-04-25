def test_qa_service_calls_run_graph(monkeypatch):
    fake = lambda u, q: {"answer": "resp"}
    monkeypatch.setattr("app.graphs.qa_graph.run_graph", fake)

    from app.services.qa_service import QAService

    svc = QAService()
    out = svc.ask("u", "q")
    assert out == {"answer": "resp"}
