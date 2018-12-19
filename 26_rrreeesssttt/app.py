from flask import Flask, request, render_template, \
                redirect, url_for, session, flash

from urllib.request import Request, urlopen
import json

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ghibli")
def ghibli():
    # Kiki's Delivery Service
    GHIBLI_URL = "http://ghibliapi.herokuapp.com/films/ea660b10-85c4-4ae3-8a5f-41cea3648e3e"

    res = urlopen(GHIBLI_URL);
    res_info = json.loads(res.read())

    title1  = res_info["title"]
    desc1 = res_info["description"]
    release1 = res_info["release_date"]

    # Princess Mononoke
    GHIBLI_URL = "http://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6"
    res = urlopen(GHIBLI_URL);
    res_info = json.loads(res.read())

    title2  = res_info["title"]
    desc2 = res_info["description"]
    release2 = res_info["release_date"]

    GHIBLI_URL = "http://ghibliapi.herokuapp.com/films/ea660b10-85c4-4ae3-8a5f-41cea3648e3e"
    return render_template("ghibli.html", title1=title1, desc1=desc1, release1=release1,
                                          title2=title2, desc2=desc2, release2=release2)

@app.route("/number")
def number():
    NUMBER_URL = "http://numbersapi.com/random/trivia"

    res = urlopen(NUMBER_URL).read().decode("utf-8")

    return render_template("number.html", fact=res)

@app.route("/dog")
def dog():
    DOG_URL = "https://random.dog/"
    
    res = urlopen(DOG_URL + "woof.json")
    res_info = json.loads(res.read())

    return render_template("dog.html", media=res_info["url"])





if __name__ == "__main__":
    app.debug = True
    app.run()
