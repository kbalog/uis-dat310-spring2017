"""
Using templates

@author: Krisztian Balog
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test")
def test():
    return render_template("base.html", users=["john", "liza", "mary"])


if __name__ == "__main__":
    app.run()
