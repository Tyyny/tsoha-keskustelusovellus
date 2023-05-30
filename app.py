from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Tähän linkit keskustelualueisiin"

@app.route("/keskustelualue1")
def page1():
    return "Tähän yksi keskustelualue"

@app.route("/keskustelualue2")
def page2():
    return "Tähän toinen keskustelualue"
