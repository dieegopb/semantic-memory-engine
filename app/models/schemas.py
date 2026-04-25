from pydantic import BaseModel

class MemoryRequest(BaseModel):
    user_id: str
    text: str

class MemoryResponse(BaseModel):
    macro: str
    category: str
    memory: str