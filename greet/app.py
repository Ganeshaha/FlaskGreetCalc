from flask import Flask, request

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