from wwr import extract_wwr_jobs
from file import save_to_file
from flask import Flask, render_template, request, redirect, send_file
from indeed import extract_indeed_jobs
from wwr import extract_wwr_jobs
from file import save_to_file

app = Flask("JobsScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="nico") 

db = {}

@app.route("/search")
def hello():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        wwr = extract_wwr_jobs(keyword)
        jobs = wwr
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)
    
@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(db[keyword])
    return send_file(f"keyword.csv", as_attachment=True)

app.run("172.20.105.157")