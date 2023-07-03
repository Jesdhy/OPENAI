import openai
from pydantic import BaseModel


class Document(BaseModel):
    prompt: str = ' '


def inference(prompt: str) -> list:
    print("PROCESSABLE")
    openai.organization = 'org-FlF7DjfN8kf6smfJafiv4p82'
    openai.api_key = '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'

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Traduce a Japones la palabra hola"},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    print("TERMINATE")
    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens
    return [content, total_tokens]
