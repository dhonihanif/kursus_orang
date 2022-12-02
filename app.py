from flask import Flask, render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "kursus"
app.secret_key='asdsdfsdfs13sdf_df%&'

mysql = MySQL(app)
@app.route("/")
def index():
    global curfet
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM login")
    curfet = cur.fetchall()
    user = [i[2] for i in curfet]
    login = False
    if "username" in session:
        login = True
    return render_template("index.html", login=login, user=user)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("name")
        password = request.form.get("password")
        user = [i[0] for i in curfet]
        pw = [i[1] for i in curfet]
        nama = [i[2] for i in curfet]
        name = nama[user.index(username)]
        if username in user and password in pw:
            session["username"] = username
            session["password"] = password
            session["nama"] = name
            return redirect(url_for("index"))
        else:
            return render_template("login.html")

    else:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        name = request.form.get("name")
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO login(username, password, name) values (%s, %s, %s)", (username, password, name))
        cur2 = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("login"))
    else:
        return render_template("register.html")

@app.route("/logout")
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

@app.route("/about")
def about():
    login = False
    if "username" in session:
        login = True
    return render_template("about.html", login=login)

@app.route("/kursus")
def service():
    login = False
    if "username" in session:
        login = True
    return render_template("kursus.html", login=login)

@app.route("/menu")
def menu():
    login = False
    if "username" in session:
        login = True
    return render_template("menu.html", login=login)

@app.route("/contact")
def contact():
    login = False
    if "username" in session:
        login = True
    return render_template("contact.html", login=login)

@app.route("/profiles")
def profiles():
    login = False
    if "username" in session:
        login = True
    return render_template("profiles.html", login=login)

@app.route("/reservation")
def reservation():
    login = False
    if "username" in session:
        login = True
    return render_template("reservation.html", login=login)

@app.route("/testimonial")
def testimonial():
    login = False
    user = [i[2] for i in curfet]
    if "username" in session:
        login = True
    return render_template("testimonial.html", login=login, user=user)

@app.route("/pesan", methods=["GET", "POST"])
def pesan():
    if request.method == "POST":
        pesan = request.form.get("pesan")
        username = session["username"]
        nama = session["nama"]
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO pesanan(pesan, username, name) values (%s, %s, '%s')" % (pesan, username, nama))
        cur2 = cur.fetchall()
        cur.close()
        return redirect(url_for("index"))
    else:
        login = False
        if "username" in session:
            login = True

        return render_template("pesan.html", login=login)

@app.route("/pesanan")
def pesanan():
    login = False
    if "username" in session:
        login = True


if __name__ == "__main__":
    app.run(debug=True)
