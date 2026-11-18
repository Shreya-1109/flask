from flask import *
app =Flask(__name__)

@app.route("/")
def url():
    return "url building task"

@app.route("/name/str")
def name():
    str = "shreya"
    return "my name is %s" %str

@app.route("/rno/num")
def roll_no():
    num = 125
    return "my roll number is %d" %num

@app.route("/age/<int:a>")
def age(a):
    return "my age is %d" %a

@app.route("/marks/<float:m>")
def marks(m):
    return "my marks is %f" %m

if __name__=="__main__":
    app.run(debug=True)