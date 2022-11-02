from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "dhoni"

mysql = MySQL(app)

@app.route("/")
def hello():
    return render_template("login.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login_post", methods=["POST"])
def login_post():
    username = request.form.get("name")
    password = request.form.get("password")
    if username == "Dhoni" and password == "123":
        return "Hello World"
    else:
        return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")
@app.route("/register_post", methods=["POST"])
def register_post():
    if request.method == "POST":
        username = request.form.get("name")
        password = request.form.get("password")
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO login values (%s, %s)" % (username, password))
        mysql.connection.commit()
        cur.close()
        return "login.html"
if __name__ == "__main__":
    app.run(debug=True)
