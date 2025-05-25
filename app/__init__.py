from flask import Flask
from flask import render_template
from flask import request
from random import randint
from flask import redirect

# Create the app
app = Flask(__name__)

# Home Page - loading a static page
@app.get("/")
def home():
    return render_template("pages/home.jinja")

# About Page - loading a static page
@app.get("/about/")
def about():
    return render_template("pages/about.jinja")

# Random Number Page - passing a value into the template
@app.get("/random/")
def random():
    randNum = randint(1, 10000)
    return render_template("pages/random.jinja", number=randNum)

# Number Page - we are getting a value from the route and passing it into the template
@app.get("/number/<int:nub>")
def analyseNumber(nub):
    print(f"You entered: {nub}")
    return render_template("pages/number.jinja", number=nub)

# Form Page - static page with a form
@app.get("/form/")
def form():
    return render_template("pages/form.jinja")

#Handle data posted from the form
@app.post("/processForm")
def processForm():
    print(f"Form data: ${request.form}")
    return render_template(
        "pages/formData.jinja",
        name = request.form["name"],
        age = request.form["age"]
    )

# Handle any missing pages
@app.errorhandler(404)
def notFound(e):
    return render_template("pages/404.jinja")

