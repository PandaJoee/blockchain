from flask import Flask, render_template, request
import sqlite3
import datetime

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    q = request.form.get("q")
    t = datetime.datetime.now()
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('INSERT INTO user (name,timestamp) VALUES(?,?)',(q,t))
    conn.commit()
    c.close()
    conn.close()
    print(q)
    return(render_template("main.html"))

@app.route("/paynow",methods=["GET","POST"])
def paynow():
    return(render_template("paynow.html"))

@app.route("/userlog",methods=["GET","POST"])
def userlog():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('select * from user')
    r=""
    for row in c:
        r = r + str(row)
    c.close()
    conn.close()
    return(render_template("userlog.html"))

@app.route("/deleteuserlog",methods=["GET","POST"])
def deleteuserlog():
    return(render_template("deleteuserlog.html"))

if __name__ == "__main__":
    app.run()
