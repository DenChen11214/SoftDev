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
    # print("-------")
    # print(search)
    # print("-------")

    res = urlopen(URL_STUB + search.replace(" ", ""))
    # print("-------")
    # print(res)
    # print(res.read())
    # print(json.loads(res.read()))
    # print("-------")

    res_info = json.loads(res.read())
    first_result = res_info["results"][0]
    # print("-------")
    # print(res_info["results"][0]["title"])
    # print("-------")

    return render_template("results.html", img_url=first_result["image_url"], 
                                           mal_link=first_result["url"],
                                           title=first_result["title"],
                                           synopsis=first_result["synopsis"],
                                           episodes=first_result["episodes"],
                                           score=first_result["score"])


if __name__ == "__main__":
    app.debug = True
    app.run()