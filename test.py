import requests
from bs4 import BeautifulSoup as bs
from indeed import extract_indeed_pages, extract_indeed_jobs

limit = 50
url = f"https://kr.indeed.com/jobs?q=python&limit={limit}"

result = requests.get(url)
soup = bs(result.text, "html.parser")
pagination = soup.find("div",{"class":"pagination"})

links = pagination.find_all('a')
pages = []

for link in links[:-1]:
  pages.append(int(link.string))

max_page = pages[-1]

next_page = soup.find("a",{"aria-label":"다음"})

if next_page.has_attr("aria-label") is True:
  start_page = limit * max_page

  req = requests.get(url)
  

def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{url}&start={page*limit}")
    soup = bs(result.text,"html.parser")
    results = soup.find_all("div",{"class":"job_seen_beacon"})
    for result in results:
      title = result.find("h2", {"class":"jobTitle"}).find("span")
      if title.has_attr("title") is not True:
        continue
      title = int(title.text)
  return jobs