from flask import Flask, render_template
from urllib.request import urlopen
import json

app = Flask(__name__)

@app.route("/")
def nasa():
    res = urlopen("https://api.nasa.gov/planetary/apod?api_key=BuBI98q6zPb0F9DTHqAkZXlSEWAKJ5A8hTTAV8qP")
    info = json.loads(res.read())
    return render_template("template.html", title=info["title"], media=info["url"], explanation=info["explanation"], media_type=info["media_type"])

if __name__ == "__main__":
    app.debug = True
    app.run()
