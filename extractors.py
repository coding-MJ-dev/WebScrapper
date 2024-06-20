from playwright.sync_api  import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

keywords = [
  "python",
  "javascript",
  "java"
]

url_list =[]

def wantedUrlListMaker(keywords) :
  for word in keywords:
    url_list.append(f'https://www.wanted.co.kr/search?query={word}&tab=position')


content_list = []

def contentsExtractor(url_list) :
  jobs_bd = []
  p = sync_playwright().start()

  browser = p.chromium.launch(headless=False) 
  page = browser.new_page()

  for url in url_list:
    page.goto(url)

    for x in range(5):
      page.keyboard.down("End")
      time.sleep(1)

    content_list.append(page.content())
  p.stop()

jobs_bd = []
def jobExtractor(content_list):
  for content in content_list:
    soup = BeautifulSoup(content, "html.parser")

    jobs = soup.find_all("div", class_="JobCard_container__REty8")

    for job in jobs:
      link = f"https://www.wanted.co.kr{job.find('a')['href']}"
      title = job.find("strong", class_="JobCard_title__HBpZf").text
      company = job.find("span", class_="JobCard_companyName__N1YrF").text
      reward = job.find("span", class_="JobCard_reward__cNlG5").text
      job = {
        "title" : title,
        "company" : company,
        "reward" : reward,
        "link" : link
      }
      jobs_bd.append(job)
    



def makeCSV(db) :
  file = open("job.csv", mode="w", encoding="utf-8")
  writer = csv.writer(file)
  writer.writerow(["title", "company", "reward", "link"])

  for job in jobs_bd:
    writer.writerow(job.values())
  file.close()


wantedUrlListMaker(keywords)

contentsExtractor(url_list)
jobExtractor(content_list)
makeCSV(jobs_bd)