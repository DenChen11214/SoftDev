from flask import Flask, render_template
from urllib.request import urlopen
import json

app = Flask(__name__)

@app.route("/")
def api():
    html = urlopen("https://api.nasa.gov/planetary/apod?api_key=BuBI98q6zPb0F9DTHqAkZXlSEWAKJ5A8hTTAV8qP")
    # print(html)
    text = json.loads(html.read())
    # print(text)
    return render_template("template.html", title=text["title"], media=text["url"])

if __name__ == "__main__":
    app.debug = True
    app.run()



# https://api.nasa.gov/planetary/apod?api_key=BuBI98q6zPb0F9DTHqAkZXlSEWAKJ5A8hTTAV8qP
