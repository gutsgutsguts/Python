from wwr import extract_wwr_jobs
from file import save_to_file
from flask import Flask, render_template

app = Flask("JobsScrapper")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/hello")
def hello():
    return 'hello you!'

app.run("172.20.105.157")