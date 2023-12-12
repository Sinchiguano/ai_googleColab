
# from crypt import methods
# from doctest import debug
from flask import Flask,redirect,url_for,flash
from flask import render_template,request,session

app = Flask(__name__)
app.secret_key = 'justonemoretime'



@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":  
        user=request.form["username"]
        password=request.form["password"]
        session["user"]=user
        session["password"]=password
        # # Flash a success message
        flash('Form submitted successfully!')
        return redirect(url_for("user",usr=user))
    else:

        # Retrieve data from the session
        user=session.get('username')
        password = session.get('password')
        # Flash a success message
        flash('Form submitted successfully!')
        if "user" and "password" :
            redirect(url_for("user"))
            # Flash a success message
            flash('Form submitted successfully!')
        return render_template("login.html")


@app.route("/user")
def user():
    # Retrieve data from the session
    # user=session.get('username')
    # password = session.get('password')
    if "user" in session:
        userTmp=session["user"]
        passwordTmp=session['password']
        flash('Form submitted successfully!')
        return render_template("sessionData.html",user=userTmp,password=passwordTmp)
    else:
        return redirect(url_for("login"))
    

@app.route("/logout")
def logout():
    flash("You have been logged out!!!","info")
    session.pop("user",None)
    flash("You have been logged out!!!","info")
    return redirect(url_for("login"))
    

if __name__ == '__main__':
    app.run(debug=True)