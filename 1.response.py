from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

res = client.chat.completions.create(
    model="qwen2.5:3b",
    messages=[{"role": "user", "content": "파이썬에서 리스트와 튜플의 차이를 한 문장으로"}],
)

print("model  :", res.model)
print("finish :", res.choices[0].finish_reason)
print("usage  :", res.usage.prompt_tokens, "/", res.usage.completion_tokens)
