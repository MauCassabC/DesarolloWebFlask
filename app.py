from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient, cursor

con = MongoClient("localhost", 27017)
db = con.Escuala
cuentas = db.alumno

app = Flask(__name__)

@app.route("/")
def index():
    cursor = cuentas.find()
    for doc in cursor:
        print(doc)

    return render_template("/login.html", data="Mau")


@app.route('/login', methods=["POST"])
def login():    
    password = request.form["password"]
    return "Esta es tu password: %s" %password 




if __name__ == "__main__":
    app.run(debug=True)

