import requests
from bs4 import BeautifulSoup as bs

limit = 50
url = "https://kr.indeed.com/jobs?q=python&limit={limit}"

def extract_indeed_pages():
  result = requests.get(url)
  soup = bs(result.text, "html.parser")
  pagination = soup.find("div",{"class":"pagination"})

  links = pagination.find_all('a')
  pages = []

  for link in links[:-1]:
    pages.append(int(link.string))

  max_page = pages[-1]
  return max_page



def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result =requests.get(f"{url}&start={page*limit}")
    print(result.status_code)
  return jobs