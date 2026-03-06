from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    q = request.args.get("q")
    print(q)
    return render_template("index.html")