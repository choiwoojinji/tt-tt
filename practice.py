# test_set
# print('hi')
# git add .
# git commit -m "메시지"
# git push 순서예요

# 처음부터 큰틀이라도 익혀봅시다
import re
import requests

SITEMAP = "https://www.dcodelab.kr/sitemap.xml"

# timeout=30 — 30초 넘게 대답이 없으면 포기한다
response = requests.get(SITEMAP, timeout=30)
xml = response.text

# <loc>주소</loc> 에서 가운데만 꺼낸다. ? 는 "최소한만 가져가라"
urls = re.findall(r"<loc>(.*?)</loc>", xml)
print("전체 주소:", len(urls))

# 이 블로그는 글 주소에만 /p/ 가 들어간다
posts = [u for u in urls if "/p/" in u]
print("글 주소:", len(posts))

for u in posts[:3]:
    print(" ", u)
