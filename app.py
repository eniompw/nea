from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        f = open("login.txt", "w")
        f.write(request.form['password'])
        f.close()
    return render_template("signup.html")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        pw = request.form['password']
        f = open("login.txt", "r")
        stored_password = f.read()
        f.close()
        if pw == stored_password:
            return "Access granted"
        else:
            return "Access denied"
    return render_template("index.html")