from flask import *
app = Flask(__name__)

@app.route("/")
def st():
    return  "login page"

@app.route("/login/<sat>")
def login(sat):
    if sat == "hr_dash":
        return redirect(url_for("hr_dash"))
    elif sat == "student_dash":
        return redirect(url_for("student_dash"))
    else:
        return "invalid input"


@app.route("/hr_dash")
def hr_dash():
    return "this is hr_dash page"

@app.route("/student_dash")
def student_dash():
    return "this is student_dash page"



if __name__ == "__main__":
    app.run(debug=True)
    