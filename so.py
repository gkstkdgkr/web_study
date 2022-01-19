import requests
from bs4 import BeautifulSoup as bs

url = "https://stackoverflow.com/jobs?q=python"

def get_last_page():
  result = requests.get(url)
  soup = bs(result.text,"html.parser")
  pages = soup.find("div",{"class":"s-pagination"}).find_all("a")
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)

def extract_job(html):
  title = html.find("h2",{"class":"mb4"}).find("a")["title"]
  company, location = html.find("h3",{"class":"mb4"}).find_all("span", recursive=False) # recursive=False 는 태그 안쪽 깊게 들어가지 않는것
  company = company.get_text(strip=True)
  location = location.get_text(strip=True)
  job_id = html['data-jobid']
  return {
    'title':title,
    'company':company,
    'location':location,
    'apply_link':f"https://stackoverflow.com/jobs/{job_id}"
  }




def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping SO: Page: {page}")
    result = requests.get(f"{url}&pg={page + 1}")
    soup = bs(result.text,"html.parser")
    results = soup.find_all("div",{"class":"-job"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs




def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs