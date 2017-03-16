"""
Using templates

@author: Krisztian Balog
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/members")
def members():
    return render_template("members.html", users=["john", "liza", "mary"])


if __name__ == "__main__":
    app.run()