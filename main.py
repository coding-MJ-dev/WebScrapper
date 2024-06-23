from flask import Flask, render_template, request, redirect, send_file
from extractors import extract_wanted_jobs
from file import save_to_file
from berlin import extract_beriln_jobs
from web3 import extract_web3_jobs
from wework import extract_wework_jobs

app = Flask("JobScrapper")

db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def hello():
    # print(request.args)
    keyword = request.args.get("keyword")
    # print(keyword)
    if keyword == None or keyword == "":
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        beriln = extract_beriln_jobs(keyword)
        web3 = extract_web3_jobs(keyword)
        wework = extract_wework_jobs(keyword)
        jobs = web3 + wework + beriln
        db[keyword] = jobs

    return render_template("search.html", keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None or keyword == "":
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)


app.run("127.0.0.1")
# app.run("0.0.0.0")
