import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"
all_jobs = []

def scrape_page(url):
  print(f"scrapping {url}...")
  response = requests.get(url=url)

  response.status_code
  # print(response.content)

  soup = BeautifulSoup(
    response.content, 
    "html.parser",
    )

  jobs = soup.find("section", class_= "jobs").find_all("li")[1:-1]
  



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


def get_pages(url):
  response = requests.get("https://weworkremotely.com/remote-full-time-jobs")
  soup = BeautifulSoup(response.content, "html.parser")
  buttons = len(soup.find("div", class_="pagination").find_all("span", class_="page"))
  return buttons


total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")

for i in range(total_pages):
  url = f"https://weworkremotely.com/remote-full-time-jobs?page={i+1}"
  # print(url)
  scrape_page(url)








print(len(all_jobs))