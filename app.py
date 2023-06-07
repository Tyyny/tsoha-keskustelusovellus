from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    alueet = ["eka", "toka"]
    return render_template("index.html", message="Alueet:", items=alueet)

@app.route("/eka")
def page1():
    return "Tähän yksi keskustelualue"

@app.route("/toka")
def page2():
    return "Tähän toinen keskustelualue"

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html", name=request.form["name"])

