def test_routes_ask_monkeypatch(monkeypatch):
    # patch QAService in the routes module
    from app.api import routes

    class FakeSvc:
        def ask(self, u, q):
            return {"answer": "ok"}

    monkeypatch.setattr("app.api.routes.QAService", lambda: FakeSvc())

    req = type("R", (), {"user_id": "u", "question": "q"})
    res = routes.ask(req)
    assert res == {"answer": "ok"}
