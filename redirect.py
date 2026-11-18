from flask import *
app = Flask(__name__)

@app.route("/")
def home():
    return "redirect process"

@app.route("/about")
def about():
    return redirect(url_for("welcome")) #it is a function name always add function name in redirect.

@app.route("/welcome") #it is a route name
def welcome():
    return "welcome to flask project"



if __name__ == "__main__":
    app.run(debug=True,port=7000)