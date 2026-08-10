from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

messages = [
    {"role": "user", "content": "청킹이 뭐야? 한 문장으로"},
]

res = client.chat.completions.create(model="qwen2.5:3b", messages=messages)
answer = res.choices[0].message.content
print("1차:", answer)

# 모델이 한 말을 목록에 다시 넣는다. 이게 있어야 이어진다
messages.append({"role": "assistant", "content": answer})
messages.append({"role": "user", "content": "그럼 그건 왜 필요해?"})

res2 = client.chat.completions.create(model="qwen2.5:3b", messages=messages)
print("2차:", res2.choices[0].message.content)
