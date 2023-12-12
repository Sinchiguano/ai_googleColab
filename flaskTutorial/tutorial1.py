from flask import Flask

from flask import redirect, url_for
from flask import render_template




app=Flask(__name__)



@app.route("/")
def home():
    return "HELLO WORLD, this is the main page!!!"


@app.route("/<tmp>")
def  user(tmp):
    name=tmp
    return f"Hello {name}"



@app.route("/admin")
def adminPage():
    print('i am here in the admin page')
    return redirect(url_for("home"))



if __name__=='__main__':
    app.run()