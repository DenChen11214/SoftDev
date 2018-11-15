from flask import Flask, request, render_template, \
                redirect, url_for, session, flash

from urllib.request import urlopen
import json

app = Flask(__name__)

URL_STUB = "https://api.jikan.moe/v3/search/anime?q="

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/results")
def results():
    search = request.args["search"]
    print("-------")
    print(search)
    print("-------")

    res = urlopen(URL_STUB + search)
    print("-------")
    print(res)
    # print(res.read())
    print(json.loads(res.read()))
    print("-------")
    # res_info = json.loads(res.read())

    # print("-------")
    # print(res_info[0])
    # print("-------")

    return "hi"

    # res = urlopen(URL_STUB.format())


if __name__ == "__main__":
    app.debug = True
    app.run()