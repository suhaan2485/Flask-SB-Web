from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    user_name = "Suhaan"
    return render_template("index.html", user_name=user_name)
