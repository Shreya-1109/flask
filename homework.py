from flask import *
app =Flask(__name__)

@app.route("/")
def courses():
    return render_template("courses.html")

@app.route("/servicess")
def services():
    return render_template("servicess.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/placements")
def placements():
    return render_template("placements.html")

if __name__=="__main__":
    app.run(debug=True)
