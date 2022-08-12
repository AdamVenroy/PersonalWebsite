from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")
