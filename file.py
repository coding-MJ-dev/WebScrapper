def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", mode="w", encoding="utf-8-sig")
    file.write("site, title, company, location, link\n")

    # writer = csv.writer(file)
    # writer.writerow(["title", "company", "reward", "link"])

    for job in jobs:
        file.write(
            f"{job['site']},{job['title']},{job['company']},{job['location']},{job['link']}\n"
        )
    file.close()
