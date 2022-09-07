# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/")
def home_page():
    return"""
    <html>
        <h1> Welcome </h1>
    </html>
    """

@app.route("/welcome")
def welcome_page():
    return"""
    <html>
        <h1> Welcome </h1>
    </html>
    """

@app.route("/welcome/home")
def welcome_home():
    return"""
    <html>
        <h1> Welcome home </h1>
    </html>
    """
@app.route("/welcome/back")
def welcome_back():
    return"""
    <html>
        <h1> Welcome back </h1>
    </html>
    """

@app.route("/add")
def add_page(a,b):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a,b)

    return str(result)

@app.route("/sub")
def sub_page(a,b):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a,b)

    return str(result)
@app.route("/mult")
def mult_page(a,b):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a,b)

    return str(result)

@app.route("/div")
def div_page(a,b):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a,b)

    return str(result)