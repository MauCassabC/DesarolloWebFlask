from flask import Flask, render_template, redirect, url_for, request
from flask.wrappers import Request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("/login.html", data="Mau")


@app.route('/login', methods=["POST"])
def login():
    password = request.form["password"]
    return "Esta es tu password: %s" %password 
    

if __name__ == "__main__":
    app.run(debug=True)