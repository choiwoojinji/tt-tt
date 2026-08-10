import numpy as np
from sentence_transformers import SentenceTransformer

data = np.load("index.npz", allow_pickle=True)
vecs, slugs, texts = data["vecs"], data["slugs"], data["texts"]

model = SentenceTransformer("intfloat/multilingual-e5-small")


def search(question, k=3):
    """질문과 가까운 조각 k 개를 찾는다."""
    qv = model.encode([question], normalize_embeddings=True)[0]
    scores = vecs @ qv

    # 17강과 다른 곳은 여기 한 줄이다. 글 단위로 묶지 않고
    # 점수 높은 순서대로 조각을 그냥 k 개 집는다
    out = []
    for i in scores.argsort()[::-1][:k]:
        out.append((float(scores[i]), str(slugs[i]), str(texts[i])))
    return out


for score, slug, text in search("조각을 겹치게 자르는 이유가 뭔가"):
    print(f"{score:.3f}  {slug}")
    print(f"        {text[:40]}")
