
from crypt import methods
from doctest import debug
from flask import Flask,redirect,url_for
from flask import render_template,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":  
        user=request.form["username"]
        password=request.form["password"]
        return redirect(url_for("user",usr=user))
    else:
        return render_template("login.html")


@app.route("/<usr>")
def user(usr):
    return f"<h2>{usr}</h1>"

    

if __name__ == '__main__':
    app.run(debug=True)