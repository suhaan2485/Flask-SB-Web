from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    user_name = "Suhaan"
    return render_template("index.html", user_name=user_name)

if __name__ == "__main__":
    app.run(debug=True, port = 5001)
   
@app.route("/testing")
def testing():
    user_name = "Sharvani"
    return render_template("index.html", user_name=user_name)