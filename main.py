from flask import Flask, render_template, request
from extractors import extract_wanted_jobs
# from extractors.berlin import extract_beriln_jobs

app = Flask("JobScrapper")

@app.route("/")
def home():
  return render_template("home.html", name="MJ")

@app.route("/search")
def hello():
  print(request.args)
  keyword = request.args.get("keyword")
  # jobs =  extract_beriln_jobs(keyword)
  jobs = extract_wanted_jobs(keyword)

  return render_template("search.html", keyword = keyword, jobs=jobs)


app.run("127.0.0.1")
