"""
 static files

@author: Krisztian Balog
"""

from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("frame.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("frame.html", page="hello", name=name)


@app.route("/input")
def input():
    return render_template("frame.html", page="input", inputval=request.args)


if __name__ == "__main__":
    app.run()
