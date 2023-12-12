from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! <h1>Hello World!!!!!</h1>'





@app.route('/login')
def login():
    return 'here you can login'


if __name__=='__main__':
    app.run(debug=True)