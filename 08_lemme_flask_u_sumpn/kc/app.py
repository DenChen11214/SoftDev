from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return '''<a href="/a"> A </a> <br>
              <a href="/b"> B </a> <br>
              <a href="/c"> C </a> <br>
    '''

@app.route("/a")
def a():
    return '<a href="/"> Back </a> <br> Ayaya'

@app.route("/b")
def b():
    return '<a href="/"> Back </a> <br> How many meters are in a parameter'

@app.route("/c")
def c():
    return '<a href="/"> Back </a> <br> What do you call a cow with no legs? <br> Ground beef.'

app.debug = True;
app.run()

if __name__ == "__main__":
    app.debug = True;
    app.run()
