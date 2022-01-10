import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&limit=50&radius=25&vjk=6c70ee2fc3122925")
#indeed_result 변수에 requests.get을 이용해서 url 정보를 저장

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
#url정보가 저장 되어있는 indeed_result 변수에서, text 파일만 불러와 indeed_soup에 저장(text파일 = html 코드)

pagination = indeed_soup.find("ul", {"class":"pagination-list"})
#url의 html코드가 저장되어있는 indeed_soup 변수에서 html구성요소가 "ul" 이며 class 이름이 "pagination-list"인 코드를 pagination 변수에 저장
print(pagination)
#pagination-list가 들어있는 변수 pagination을 출력

pages = pagination.find_all('a')
#pages 변수를 만들어 pagination-list(html코드)안의 a(링크)부분을 저장함

print(pages)
#a 링크 출력

spans = []
#pages 를 하나하나 넣을 리스트 spans 선언

for page in pages: #pages 변수 안에 있는 요소 하나하나를
  spans.append(page.find("span")) #spans 리스트에 넣어줌
print(spans[:-1]) #마지막 하나 빼고 처음부터 출력