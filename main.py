import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

response = requests.get(url=url)

response.status_code
# print(response.content)

soup = BeautifulSoup(
  response.content, 
  "html.parser",
  )

jobs = soup.find("section", class_= "jobs").find_all("li")[1:-1]

all_jobs = []

for job in jobs:
  title = job.find("span", class_="title").text
  companies = job.find_all("span", class_="company")
  company = companies[0].text
  position = companies[1].text
  region = companies[2].text
  url = job.find("div", class_="tooltip--flag-logo").next_sibling.get('href')  # [] get attribut not text
  # url = job.find("a")
  # if url:
  #   url = url["href"]
  
  job_data = {
    "title": title,
    "company": companies[0].text,
    "position": companies[1].text,
    "region": companies[2].text,
    "url": f"https://weworkremotely.com/{url}",
  }
  all_jobs.append(job_data)

print(all_jobs)

