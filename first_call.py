from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",   # 내 컴퓨터의 Ollama
    api_key="ollama",                       # 로컬은 검사 안 한다. 아무 글자나
)

res = client.chat.completions.create(
    model="qwen2.5:3b",
    messages=[
        {"role": "user", "content": "파이썬에서 리스트와 튜플의 차이를 한 문장으로"},
    ],
)

print(res.choices[0].message.content)

