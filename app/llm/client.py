# app/llm/client.py

from openai import OpenAI

client = OpenAI()

def generate_response(prompt: str) -> str:
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente útil."},
            {"role": "user", "content": prompt}
        ]
    )

    return resp.choices[0].message.content