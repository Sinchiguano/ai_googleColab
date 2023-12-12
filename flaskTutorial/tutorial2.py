from flask import Flask
from flask import redirect, url_for
from flask import render_template




app=Flask(__name__)



@app.route("/<name>")
def home(name):
    return render_template("base.html",tmp=name,aux=5)


@app.route("/back")
def back():
    return render_template("base.html",tmp1=['carlos','juan','pedro'])


if __name__=='__main__':
    app.run()