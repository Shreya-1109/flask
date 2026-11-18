from flask import *
app = Flask(__name__)

@app.route("/")
def home():
    return "this is home page"

@app.route("/kitchen")
def kitchen():
    return "this is my kitchen"

@app.route("/hall")
def hall():
    return redirect(url_for("kitchen"))

if __name__ =="__main__":
    app.run(debug=True)