from flask import Flask, render_template, request
import time, matplotlib.pyplot as plt

from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config['MYSQL_DB'] = "counter"

mysql = MySQL(app)

now = time.strftime("%A, %d %B, %Y at %X")

@app.route('/' ,methods =["GET","POST"])
def index():
     if request.method == "POST":
        password = request.form.get('password')
        email = request.form['email']


        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO lista (email, password ) VALUES (%s,%s )",(email,password))
        cur.close()

        mysql.connection.commit()

        return render_template("site.html")
     return render_template("index.html", now=now)


if __name__ == "__main__":
   app.run(debug=True)