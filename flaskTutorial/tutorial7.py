
# from crypt import methods
# from doctest import debug
from flask import Flask,redirect,url_for,flash
from flask import render_template,request,session
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.secret_key = 'justonemoretime'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite://users.sqlite3'

df=SQLAlchemy(app)


class users(df.Model):
    # _id=df.column("id",df.Integer,primary_key=True)
    name=df.column("name",df.String(100))
    email=df.Column("email",df.String)

    def __init__(self,name,email):
        #constructor
        self.name=name
        self.email=email


@app.route('/')
def home():
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


@app.route("/user",methods=["POST","GET"])
def user():
    # Retrieve data from the session
    # user=session.get('username')
    # password = session.get('password')
    email=None
    if "user" in session:
        userTmp=session["user"]
        passwordTmp=session['password']

        if request.method=="POST":
            email=request.form["email"]
            session["email"]=email
            flash('Form submitted successfully!')
        else:
            if "email" in session:
                email=session["email"]
        return render_template("sessionData.html",email=email)
    else:
        return redirect(url_for("login"))
    

@app.route("/logout")
def logout():
    flash("You have been logged out!!!","info")
    session.pop("user",None)
    session.pop("email",None)
    flash("You have been logged out!!!","info")
    return redirect(url_for("login"))
    

if __name__ == '__main__':
    df.create_all()
    app.run(debug=True)