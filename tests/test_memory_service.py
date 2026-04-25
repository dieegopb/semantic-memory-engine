from app.services.memory_service import MemoryService


def test_get_user_memory_existing():
    svc = MemoryService()
    mem = svc.get_user_memory("123")
    assert isinstance(mem, list)
    assert any("Usuário gosta" in m for m in mem)


def test_get_user_memory_missing():
    svc = MemoryService()
    assert svc.get_user_memory("no-user") == []
