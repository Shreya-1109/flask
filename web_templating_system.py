from flask import *
app = Flask(__name__)

@app.route("/")
def home():
    return "web templating system"

@app.route("/mo")
def mo():
    num=234
    return render_template("mo.html",n=num )

@app.route("/test2")
def test2():
    name="shreya"
    return render_template("test2.html",name=name)

@app.route("/test3")
def test3():
    stu_list=[11,"hii",True,56.6]
    return render_template("test3.html",list=stu_list)

@app.route("/test4")
def test4():
    stu_dict={"id":1,"name":"shreya","city":"pune"}
    return render_template("test4.html",list=stu_dict)

    

if __name__ =="__main__":
    app.run(debug=True)