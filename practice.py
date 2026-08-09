# test_set
# print('hi')
# git add .
# git commit -m "메시지"
# git push 순서예요

# 처음부터 큰틀이라도 익혀봅시다
import pathlib
from langchain_text_splitters import RecursiveCharacterTextSplitter

texts = {
    p.stem: p.read_test(encoding='utf-8') # 인코딩은 utf-8 로 함
    for p in sorted(pathlib.Path("posts").glob("*.md")) 
    # 원본보존하고 복사로 정렬함 posts 파일안에 md파일 전부 가지고오겠다
}

