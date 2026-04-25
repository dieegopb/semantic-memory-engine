import types
import pytest


class DummyResp:
    def __init__(self, data=None, ok=True):
        self._data = data or {}
        self._ok = ok

    def raise_for_status(self):
        if not self._ok:
            raise Exception("bad response")

    def json(self):
        return self._data


def test_search_no_api_key(monkeypatch):
    monkeypatch.delenv("SERPER_API_KEY", raising=False)
    from app.services.search_service import SearchService

    svc = SearchService()
    assert svc.search("anything") == []


def test_search_success(monkeypatch):
    monkeypatch.setenv("SERPER_API_KEY", "key")

    def fake_post(*a, **k):
        return DummyResp({"organic": [{"snippet": "one"}, {"snippet": "two"}]})

    monkeypatch.setattr("requests.post", fake_post)
    from app.services.search_service import SearchService

    svc = SearchService()
    results = svc.search("q")
    assert results == ["one", "two"]


def test_search_request_exception(monkeypatch):
    monkeypatch.setenv("SERPER_API_KEY", "key")

    def bad(*a, **k):
        raise Exception("network")

    monkeypatch.setattr("requests.post", bad)
    from app.services.search_service import SearchService

    svc = SearchService()
    assert svc.search("q") == []
