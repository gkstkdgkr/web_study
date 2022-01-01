import requests
import bs4

indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&limit=50")



# print(indeed_result.text) # response [200] = okay