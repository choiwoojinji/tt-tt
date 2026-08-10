# get one posts 뷰티풀숲으로 본문 찾기
import requests
from bs4 import BeautifulSoup                      # 설치는 beautifulsoup4, 부를 땐 bs4
from markdownify import markdownify as to_md

url = "https://www.dcodelab.kr/p/git-21-branch"

html = requests.get(url, timeout=30).text
soup = BeautifulSoup(html, "html.parser")

# select_one — 조건에 맞는 것 중 첫 번째 하나
body = soup.select_one("div.prose")
print("본문 찾음:", body is not None)

# select — 조건에 맞는 것 전부. 버튼·아이콘은 글이 아니라 지운다
for junk in body.select("button, svg, script, style"):
    junk.decompose()

md = to_md(str(body), heading_style="ATX")

print(len(md), "자")
print(md[:120])

