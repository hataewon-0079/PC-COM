import os
import sys
import urllib.request
client_id = "HzGdkN75ibQ9mP44ZcsN"
client_secret = ""
encText = urllib.parse.quote("개인정보")
url = "https://openapi.naver.com/v1/search/news.json?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)


# 위 결과 값 파싱
import json
json_result = json.loads(response_body)
print(json_result)

# 위 결과 값에서 필요한 값만 추출
for item in json_result['items']:
	print(item['title'], item['link'])


# 위 결과 값에서 필요한 값만 추출하여 html 파일로 저장

html = """`
<!DOCTYPE html>
<html>
<head>
	<title>News</title>
</head>
<body>
	<h1>News</h1>
	<ul>
"""
for item in json_result['items']:
	html += f"<li><a href='{item['link']}'>{item['title']}</a></li><br>"
html += """
	</ul>
</body>
</html>
"""
with open("d:\\news.html", "w", encoding="utf-8") as file:
	file.write(html)
print("저장완료")







