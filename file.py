def save_to_file(file_name, jobs):
  file = open(f"{file_name}.csv", mode="w", encoding="utf-8")
  file.write("title, company, reward, link\n")

  # writer = csv.writer(file)
  # writer.writerow(["title", "company", "reward", "link"])

  for job in jobs:
    file.write(f"{job['title']},{job['company']},{job['reward']},{job['link']} \n")
  file.close()  