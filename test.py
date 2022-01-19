import requests
from bs4 import BeautifulSoup as bs

limit = 50
url = "https://kr.indeed.com/jobs?q=python&limit=900"


result = requests.get(url)
soup = bs(result.text, "html.parser")
pagination = soup.find("div",{"class":"pagination"})

links = pagination.find_all('a')
pages = []

next_page = pagination.find('svg')
print(next_page)
if next_page is not None:
  print("a")

for link in links[:-1]:
  pages.append(int(link.string))

max_page = pages[-1]

