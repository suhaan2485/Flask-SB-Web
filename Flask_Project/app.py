from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    project_name= "Suhaan's Web Portal"
    return render_template("index.html", project_name=project_name)

   
@app.route("/testing")
def testing():
    test_display = "Advanced Web Features in progres....."
    return render_template("testing.html", test_display=test_display)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, port = 5003)