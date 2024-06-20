from extractors import *
from file import save_to_file

keyword = str(input("what do you want search for? "))

wanted = extract_wanted_jobs(keyword)
# indeed = extract_indeed_jobs(keyword)
# wwr = extract_indeed_jobs(keyword)
# jobs = indeed + wwr

save_to_file(keyword, wanted)
# file = open(f"{keyword}".csv, "w")
# file.write("")
