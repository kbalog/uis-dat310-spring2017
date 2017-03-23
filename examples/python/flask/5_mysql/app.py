"""
Using MySQL

@author: Krisztian Balog
"""

from flask import Flask, render_template, g
import mysql.connector

app = Flask(__name__)

CONFIG = {"MYSQL_DATABASE_USER": "root",
          "MYSQL_DATABASE_PASSWORD": "root",
          "MYSQL_DATABASE_DB": "dat310",
          "MYSQL_DATABASE_HOST": "localhost"}
conn = mysql.connector.connect(host=CONFIG["MYSQL_DATABASE_HOST"], user=CONFIG["MYSQL_DATABASE_USER"],
                               password=CONFIG["MYSQL_DATABASE_PASSWORD"], database=CONFIG["MYSQL_DATABASE_DB"])


@app.before_request
def db_connect():
    """Build up a MySQL connection before each request."""
    g.conn = mysql.connect()


@app.teardown_request
def db_disconnect(exception=None):
    """Close MySQL connection after each request."""
    g.conn.close()

@app.teardown_appcontext


@app.route("/init")
def init():
    """Create table and initialize with some data."""
    cur = g.conn.cursor()
    try:
        sql = "CREATE TABLE postcodes (postcode VARCHAR(4), location VARCHAR(20), PRIMARY KEY(postcode))"
        cur.execute(sql)
    except mysql.connector.Error as err:
        render_template("error.html", msg=err)
    finally:
        cur.close()

    return render_template("success.html", msg="Successful initialization")


@app.route("/listall")
def list_all():
    cur = g.conn.cursor()
    cur.execute("SELECT , year, rating FROM movies")
    rv = cur.fetchall()
    print(rv)
    cur.close()


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
