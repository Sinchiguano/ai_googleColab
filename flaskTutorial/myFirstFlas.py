from flask import Flask, redirect, url_for
import flask

# ctrl +k +c to comment several lines 
# ctrl +k +u uncomment several lines

# Print the version
print(f"Flask version: {flask.__version__}")
print("Flask version: {}".format(flask.__version__))




app=Flask(__name__)



@app.route("/")
def home():
    return "Hello! this is the main page <h1>HELLO<h1>"


@app.route("/<name>")
def user(name):
    return  f"Hello{name}"


@app.route("/admin")
def admin():
    return redirect(url_for("/home"))



if __name__=='__main__':
    app.run()