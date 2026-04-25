from typing import TypedDict, List, Optional

class QAState(TypedDict):
    user_id: str
    question: str

    memory: List[str]
    web_results: List[str]

    answer: Optional[str]