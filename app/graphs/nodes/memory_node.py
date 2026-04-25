from app.services.memory_service import MemoryService

def memory_node(state):
    service = MemoryService()

    memory = service.get_user_memory(state["user_id"])

    return {
        **state,
        "memory": memory
    }