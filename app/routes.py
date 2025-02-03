from flask import render_template
from random import randint
from app import app

@app.route("/")
def index():
    return render_template("index.html")

# ...existing code for other routes...
