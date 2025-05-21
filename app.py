from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
from flask_cors import CORS

app = Flask(__name__, static_url_path='/assets', static_folder='assets')
app.secret_key = "super_secret_key"
CORS(app)

# Init DB
def init_db():
    with sqlite3.connect("users.db") as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            );
        ''')
init_db()

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()

        if user:
            if user[3] == password:
                session["user"] = user[1]  # username
                return redirect("/main")
            else:
                return render_template("login.html", error="Wrong password")
        else:
            session["temp_email"] = email
            session["temp_password"] = password
            return redirect("/register")

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/register-user", methods=["POST"])
def register_user():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
            conn.commit()
            session["user"] = username
            return redirect("/main")
        except sqlite3.IntegrityError:
            return "User already exists. Try logging in."

@app.route("/main")
def main():
    if "user" not in session:
        return redirect("/")
    return render_template("main.html", username=session["user"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)
