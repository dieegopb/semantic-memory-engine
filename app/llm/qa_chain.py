from langchain_openai import ChatOpenAI

def answer_with_context(question: str, web_context: list[str], memory_context: list[str]):

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    web_text = "\n".join(web_context)
    memory_text = "\n".join(memory_context)

    prompt = f"""
    Você é um assistente inteligente.

    Use:
    - informações da internet (WEB)
    - memórias do usuário (MEMORY)

    Regras:
    - Priorize MEMORY quando relevante
    - Use WEB para complementar
    - Não invente informações
    - Seja direto

    MEMORY:
    {memory_text}

    WEB:
    {web_text}

    PERGUNTA:
    {question}
    """

    response = llm.invoke(prompt)

    return response.content