from flask import Flask, request, render_template, \
                redirect, url_for, session, flash

from urllib.request import urlopen
import json

app = Flask(__name__)

# Kiki's Delivery Service
GHIBLI_URL = "http://ghibliapi.herokuapp.com/films/ea660b10-85c4-4ae3-8a5f-41cea3648e3e"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ghibli")
def ghibli():
    res = urlopen(GHIBLI_URL);
    res_info = json.loads(res.read())





if __name__ == "__main__":
    app.debug = True
    app.run()
