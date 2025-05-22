from flask import Flask
from flask import render_template
from random import randint
from flask import redirect

# Create the app
app = Flask(__name__)


@app.get("/")
def home():
    return render_template("pages/home.jinja")

@app.get("/about/")
def about():
    return render_template("pages/about.jinja")

@app.get("/random/")
def random():
    randNum = randint(1, 100000000000000000)
    return render_template("pages/random.jinja", number=randNum)

@app.get("/number/<int:nub>")
def analyseNumber(nub):
    print(f"You entered: {nub}")
    return render_template("pages/number.jinja", number=nub)

@app.get("/form/")
def form():
    return render_template("pages/form.jinja")

@app.errorhandler(404)
def notFound(e):
    return render_template("pages/404.jinja")

