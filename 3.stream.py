from openai import OpenAI
import time

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

t = time.perf_counter()
first = None

stream = client.chat.completions.create(
    model="qwen2.5:3b",
    messages=[{"role": "user", "content": "내가 무엇을 하는 사람인지 기억해?"}],
    stream=True,                    # 이 한 줄이 전부다
)

for chunk in stream:
    piece = chunk.choices[0].delta.content or ""     # 없으면 빈 문자열
    if piece and first is None:
        first = time.perf_counter() - t
    print(piece, end="", flush=True)                 # 줄바꿈 없이 이어 찍는다

print()
print(f"첫 글자 {first:.1f}초 / 전체 {time.perf_counter() - t:.1f}초")
