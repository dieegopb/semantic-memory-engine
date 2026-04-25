# app/graphs/nodes/llm_node.py

from app.llm.client import generate_response

def llm_node(state):
    prompt = f"""
Pergunta: {state['question']}
Memória: {state.get('memory', [])}
Web: {state.get('web_results', [])}
"""

    answer = generate_response(prompt)

    return {"answer": answer}