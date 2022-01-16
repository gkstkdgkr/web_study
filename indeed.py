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
    print(f"Scrapping page {page}")
    result =requests.get(f"{url}&start={page*limit}")
    soup = bs(result.text, "html.parser")
    results = soup.find_all("a",{"class":"result"})
    for result in results:
      title = result.find("h2",{"class":"jobTitle"})
      title_span = title.find("span")
      if title_span.has_attr("title") is True:
        title = str(title_span.string)
      else:
        continue
      company = result.find("span",{"class":"companyName"})
      if company is not None:
        company = str(company.string)
      else:
        company = str(company.find("a",{"class":"companyOverviewLink"}).string)
      location = result.find("div",{"class":"companyLocation"}).text
      job_id = result["data-jk"]
      job = {
        'title':title, 
        'company':company, 
        'location':location, 
        'link':f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50&vjk={job_id}"
      }
      jobs.append(job)

      
  return jobs