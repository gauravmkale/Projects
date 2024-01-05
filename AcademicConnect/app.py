import os
import json

import sqlite3
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename


from datetime import datetime, timezone
from helpers import apology, login_required


# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
con = sqlite3.connect("users.db",check_same_thread=False)
cur = con.cursor()
con.row_factory = sqlite3.Row


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/sell",methods=["GET","POST"])
def sell():
    print(request.form)
    if request.method == 'POST':
        # Get form data
        year = request.form['year']
        branch = request.form['branch']
        resourcetype = request.form['resourcetype']
        bookname = request.form['bookname']
        price = request.form['price']
        number = request.form['number']

        # Get the file from the request
        photo = request.files['photo']
        filename = secure_filename(photo.filename)
        photo_path = os.path.join(app.root_path, 'static/uploads', filename)
        photo.save(photo_path)
        absolute_path = photo_path
        workspace_path = '/workspaces/96624731/pset10/'
        # Replace the workspace path with an empty string
        relative_path = absolute_path.replace(workspace_path, '')

        user_id = session["user_id"]

        # Check if the file is present and allowed
        if photo and allowed_file(photo.filename):
            # Save data to MySQL along with the photo
            cur.execute(
                "INSERT INTO resources (year, branch, resourcetype, bookname, price, number, photo,user_id) "
                "VALUES (:year, :branch, :resourcetype, :bookname, :price, :number, :photo, :user_id)",
                {"year": year, "branch": branch, "resourcetype": resourcetype, "bookname": bookname, "price": price, "number": number, "photo": relative_path, "user_id": user_id}
            )
            con.commit()

            return redirect(('/'))
    else:
        return render_template('sell.html')

def allowed_file(filename):
    # Check if the file extension is allowed
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


@app.route("/contact",methods=["GET","POST"])
def contact():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        message=request.form.get("message")
        if not name or not email or not message:
            flash(f"Please fill the details before submitting the form")
            return redirect("/")

        else:
            cur.execute(
                "INSERT INTO feedback (name,email,message) VALUES (?,?,?)",(name,email,message))
            con.commit()
            flash(f"Feedback submitted successfully")
            return redirect("/")


    else:
        return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/my")
@login_required
def my():
    # Retrieve the user's books from the database
    user_id = session["user_id"]
    cur.execute("SELECT * FROM resources WHERE user_id = ?", (user_id,))
    user_books=cur.fetchall()
    con.commit()
    return render_template("my.html", user_books=user_books)


@app.route("/buy")
def buy():
    # Query the database to get information about available books
    cur.execute("SELECT * FROM resources")
    books=cur.fetchall()
    print("books:", books)
    con.commit()

    # Render the buy.html template with the book information
    return render_template("buy.html", books=books)
@app.route("/login", methods=["GET", "POST"])
def login():
    # Forget existing user id
    session.clear()

    # User reached via submitting a form via post
    if request.method == "POST":
        if not request.form.get("username"):
            flash("Must provide username")
            return render_template("login.html")
        if not request.form.get("password"):
            flash("Must provide password")
            return render_template("login.html")

        username = request.form.get("username")
        cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        rows = cur.fetchall()

        if len(rows) != 1:
            flash("Invalid username or password")
            return render_template("login.html")

        stored_hash = rows[0][2]
        entered_password = request.form.get("password")

        print("Stored Hash:", stored_hash)
        print("Entered Password:", entered_password)

        if not check_password_hash(stored_hash, entered_password):
            flash("Invalid username or password")
            return render_template("login.html")

        # Remember which user has logged in
        session["user_id"] = rows[0][0]

        # Redirect user to home page
        return render_template("index.html")

    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()

    if request.method == "POST":
        username=request.form.get("username")
        password=request.form.get("password")
        confirmation=request.form.get("confirmation")
        branch=request.form.get("branch")
        year=request.form.get("year")

        if not username or not password or not confirmation:
            flash("Input can't be blank")
            return render_template("register.html")

        # Check if the password and confirmation match
        if password != confirmation:
            flash("Password and confirmation must match")
            return render_template("register.html")

        # Check if the username is already taken
        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        existing_user = cur.fetchone()
        if existing_user:
            flash("Username is already taken")
            return render_template("register.html")
        else:
            cur.execute(
                #Creating new row for new user
                "INSERT INTO users (username, hash, year, branch) VALUES (?, ?, ?,?)",(
                username,
                generate_password_hash(request.form.get("password")), year,branch),
            )
            con.commit()
        #Logging user in
        cur.execute("SELECT * FROM users WHERE username=?",(username,))
        rows=cur.fetchall()
        #remember user has logged in
        session["id"]=rows[0][0]
        # return user to homepage
        flash(f"YOU ARE REGISTERED as {username}")
        return render_template("login.html")
    else:
        return render_template("register.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/password", methods=["GET", "POST"])
@login_required
def password():
    """Show settings"""

    if request.method == "POST":

        # Validate submission
        currentpassword = request.form.get("currentpassword")
        newpassword = request.form.get("newpassword")
        confirmation = request.form.get("confirmation")

        # Query database for username
        cur.execute("SELECT * FROM users WHERE id = ?", (session["user_id"],))
        rows = cur.fetchall()

        # Ensure password == confirmation
        if not (newpassword == confirmation):
            flash(f"The passwords do not match")

        # Ensure password not blank
        if currentpassword == "" or newpassword == "" or confirmation == "":
            flash(f"Input is blank")

       # Ensure password is correct
        if not check_password_hash(rows[0][2], currentpassword):
            flash(f"Invalid password")
        else:
            hashcode = generate_password_hash(newpassword, method='pbkdf2:sha256', salt_length=8)
            cur.execute("UPDATE users SET hash = ? WHERE id = ?", (hashcode, session["user_id"]))
            con.commit()
        # Redirect user to settings
        return redirect("/account")

    else:
        return render_template("password.html")


@app.route("/account")
@login_required
def account():
    """Show account"""
    # Query database
    user_id = session["user_id"]

    # Assuming you have a 'users' table with columns: id, username, year, branch
    cur.execute("SELECT username, year, branch FROM users WHERE id = ?", (user_id,))
    user_info = cur.fetchone()

    if user_info:
        username = user_info[0]
        year = user_info[1]
        branch = user_info[2]
        return render_template("account.html", username=username, year=year, branch=branch)
    else:
        # Handle the case when the user is not found
        flash("User not found.")
        return redirect(url_for("index"))  # Redirect to the homepage or another appropriate page