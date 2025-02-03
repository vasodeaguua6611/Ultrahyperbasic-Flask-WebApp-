from flask import Flask, render_template
app = Flask(__name__)

@app.route("/hello/")
@app.route("/hello/<string:name>/")
def hello(name=None):
    return render_template("index.html")

if __name__ == "__main__":
    app.run()