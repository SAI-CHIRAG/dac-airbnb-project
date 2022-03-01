from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)


@app.route("/")
def hello_page():
    return render_template('home.html')


@app.route("/login")
def login_page():
    return render_template('login.html')


@app.route("/register")
def register_page():
    return render_template('register.html')
