from app.graphs.qa_graph import run_graph

class QAService:

    def ask(self, user_id: str, question: str):
        return run_graph(user_id, question)