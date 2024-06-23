import requests
from bs4 import BeautifulSoup


def get_number(url):
    page = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        },
    )
    soup = BeautifulSoup(
        page.content,
        "html.parser",
    )
    if soup.find_all("a", class_="page-numbers"):
        return len(soup.find_all("a", class_="page-numbers"))
    return 1


def scrape_page(paths):
    job_db = []
    for skill in paths:
        page = requests.get(
            skill,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
            },
        )
        soup = BeautifulSoup(
            page.content,
            "html.parser",
        )

        jobs = soup.find_all("li", class_="feature")
        for job in jobs:
            company = job.find("span", class_="company").text
            title = job.find("span", class_="title").text
            loaction = job.find("span", class_="region").text
            link = job.find("a").get("href")
            print(loaction)
            job_data = {
                "site": "wework",
                "title": title.replace(",", " "),
                "company": company.strip().replace(",", " "),
                "location": loaction.replace("/", " "),
                "link": f"https://weworkremotely.com{link}",
            }
            job_db.append(job_data)

        return job_db


def extract_wework_jobs(keyword):
    paths = [
        f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={keyword}"
    ]
    job_db = scrape_page(paths)
    return job_db
