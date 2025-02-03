from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello/")
@app.route("/hello/<string:name>/")
def hello(name=None):
    quotes = [
        "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann",
        "'BUY GOLD'",
        "'pipis 2'",
        "'no kromer' -- Unknown",
        "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
        "HaLLO!!!!!!!"
    ]
    randomNumber = randint(0, len(quotes) - 1)
    quote = quotes[randomNumber]
    return render_template('test.html', **locals())

@app.route("/members")
def members():
    members_list = ["yo", "xuya", "myself"]
    return render_template('members.html', members=members_list)

@app.route("/members/<string:name>/")
def getMember(name):
    return name

if __name__ == "__main__":
    app.run(debug=True)