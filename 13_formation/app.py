# Johnson Li
# SoftDev1 pd8
# K13 -- Echo Echo Echo 
# 2018-09-27

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    # root route with form
    return render_template("form.html")

@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    # each needed field is assigned to a var
    reqMethod = request.method
    if reqMethod == 'GET':
        username = request.args['username']
    elif reqMethod == 'POST':
        username = request.form['username']
    greeting = "HI " + username.upper();

    # return the html page using a template
    return render_template("response.html", 
                            username = username, 
                            reqMethod = reqMethod, 
                            greeting = greeting);

app.debug = True;
app.run()

if __name__ == "__main__":
    app.debug = True;
    app.run()
