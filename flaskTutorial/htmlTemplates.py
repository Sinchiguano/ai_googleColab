from flask import Flask, redirect, url_for, render_template
import flask

# ctrl +k +c to comment several lines 
# ctrl +k +u uncomment several lines

# Print the version
# print(f"Flask version: {flask.__version__}")
# print("Flask version: {}".format(flask.__version__))




app=Flask(__name__)



@app.route("/<name>")
def home(name):
    return render_template("index.html", content=name,tmp=3)



if __name__=='__main__':
    app.run()