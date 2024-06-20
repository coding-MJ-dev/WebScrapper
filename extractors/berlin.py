import requests
from bs4 import BeautifulSoup

def get_number(url):
    page = requests.get(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    })
    soup = BeautifulSoup(page.content, "html.parser",)
    if (soup.find_all("a", class_="page-numbers")):
      return len(soup.find_all("a", class_="page-numbers"))
    return 1



page_num = get_number("https://berlinstartupjobs.com/engineering/")
paths = [f"https://berlinstartupjobs.com/engineering/page/{i+1}/" for i in range(page_num)]

def get_url(keyword):
  number = get_number(f"https://berlinstartupjobs.com/skill-areas/{keyword}")
  for i in range(number):
    paths.append(f"https://berlinstartupjobs.com/skill-areas/{keyword}/page/{i+1}/")
  
  return paths


def scrape_page(paths):
  job_db = []
  for skill in paths:
    page = requests.get(skill, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    })
    print(f"this page is {skill}")
    soup = BeautifulSoup(page.content, "html.parser",)

    jobs = soup.find_all("li", class_="bjs-jlid")
    for job in jobs:
      company = job.find("a", class_="bjs-jlid__b").text
      title = job.find("h4", class_="bjs-jlid__h").find("a").text
      url = job.find("h4", class_="bjs-jlid__h").find("a").get('href')
      desc = job.find("div", class_="bjs-jlid__description").text
      job_data = {
        "title": title,
        "company": company,
        "url": f"{url}",
        "desc": desc,
      }
      job_db.append(job_data)

    return job_db



# get_url(skills)

# scrape_page(paths)

def extract_beriln_jobs(keyword):
  paths = get_url(keyword)
  job_db = scrape_page(paths)
  return job_db



# page = requests.get("https://berlinstartupjobs.com/skill-areas/python/", headers={
# "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
# })
# print(f"this page is python")

# soup = BeautifulSoup(page.content, "html.parser",)

# jobs = soup.find_all("li", class_="bjs-jlid")
# for job in jobs:
#   company = job.find("a", class_="bjs-jlid__b").text
#   position = job.find("h4", class_="bjs-jlid__h").find("a").text
#   url = job.find("h4", class_="bjs-jlid__h").find("a").get('href')
#   print(position, url, company)

  