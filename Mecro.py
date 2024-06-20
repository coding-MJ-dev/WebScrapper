from playwright.sync_api  import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

p = sync_playwright().start()

browser = p.chromium.launch(headless=False) # headless=False 가 되면 실제로 화면을 볼 수 있음 
#headless's default == true

page = browser.new_page()

page.goto('https://www.wanted.co.kr/search?query=flutter&tab=position')

# 만약 매크로를 만들고 싶다면!!
# time.sleep(3)

# #Aside_searchButton__rajGo라는 class의 button을 누르시오
# page.click("button.Aside_searchButton__rajGo")
# time.sleep(3)


# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")
# time.sleep(2)

# page.keyboard.down("Enter")
# time.sleep(3)

# #search_tab_position 를 id로 가진 a를 누르시오
# page.click("a#search_tab_position")
# time.sleep(3)

# can get the screenshot of a browser
# page.screenshot(path="screenshot.png")

for x in range(5):
  page.keyboard.down("End")
  time.sleep(3)

content = page.content()
p.stop()

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_="JobCard_container__REty8")

jobs_bd = []

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

# print(jobs_bd)
# print(len(jobs_bd))

#file name, default mode is only "r" - read. so it should be changed to "w"
file = open("job.csv", mode="w", encoding="utf-8")
writer = csv.writer(file)
writer.writerow(["title", "company", "reward", "link"])

for job in jobs_bd:
  writer.writerow(job.values())
file.close()


keywords = [
  "flutter",
  "react",
  "kotlin"
]