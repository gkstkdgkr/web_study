import requests
from bs4 import BeautifulSoup as bs
from indeed import extract_indeed_pages, extract_indeed_jobs

limit = 50
url = "https://kr.indeed.com/jobs?q=python&limit={limit}"

last_indeed_page = extract_indeed_pages()

jobs = []
for page in range(last_indeed_page):
  result = requests.get(f"{url}&start={page*limit}")
  soup = bs(result.text,"html.parser")
  results = soup.find_all("div",{"class":"job_seen_beacon"})
  for result in results:
    title = result.find("h2", {"class":"jobTitle"}).find("span")
    if title.has_attr("title") is not True:
      continue
    title = title.text
    print(title)
