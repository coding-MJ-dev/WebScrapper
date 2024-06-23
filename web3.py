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


paths = []


def get_url(keyword):
    number = get_number(f"https://web3.career/{keyword}-jobs")
    for i in range(number):
        paths.append(f"https://web3.career/{keyword}-jobs?page={i+1}")
    return paths


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

        jobs = soup.find_all("tr", class_="table_row")
        for job in jobs:
            index = job.find("div", class_="job-title-mobile").get("data-jobid")
            if index != None:
                link = (
                    job.find("div", attrs={"data-jobid": index}).find("a").get("href")
                )
                company = job.find("td", class_="job-location-mobile").find("a").text
                # company = job.find("a", href=link).find("h2").text
                title = job.find("h2", class_="my-primary").text
                loaction = "Remote"
                if index:
                    td1 = job.find("td", attrs={"data-jobid": index}).find_next_sibling(
                        "td"
                    )
                    td2 = td1.find_next_sibling("td") if td1 else None
                    td3 = td2.find_next_sibling("td") if td2 else None
                    if td3 and td3.find("a"):
                        loaction = td3.find("a").text

                job_data = {
                    "site": "web3.career",
                    "title": title.replace(",", " "),
                    "company": company.strip().replace(",", " "),
                    "location": loaction,
                    "link": f"https://web3.career/{link}",
                }
                job_db.append(job_data)
            else:
                continue

        return job_db


# get_url(skills)

# scrape_page(paths)


def extract_web3_jobs(keyword):
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
