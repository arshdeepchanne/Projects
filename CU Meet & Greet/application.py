import os

import mysql.connector
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Connect database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="rootpassword"
)


@app.route("/")
# @login_required
def index():
    # """Show portfolio of stocks"""

    # # Query the database for logged in user's stock holdings
    # portfolio = db.execute("SELECT symbol, total_shares FROM stocks WHERE user_id=?", session["user_id"])

    # # Query the database for logged in user's cash
    # cash = db.execute("SELECT cash FROM users WHERE id=?", session["user_id"])

    # cash_left = cash[0]["cash"]

    # # Look up the current price of each stock and calculate the total holdings of the user
    # total_holdings = 0
    # for stock in portfolio:
    #     quote = lookup(stock["symbol"])
    #     stock["name"] = quote["name"]
    #     stock["price"] = quote["price"]
    #     stock["total_hold"] = stock["price"] * stock["total_shares"]
    #     total_holdings += stock["total_hold"]

    # total_holdings += cash_left

    # return render_template("index.html", portfolio=portfolio, cash=cash_left, total=total_holdings)
    return render_template("index.html")


# @app.route("/buy", methods=["GET", "POST"])
# @login_required
# def buy():
#     """Buy shares of stock"""

#     if request.method == "POST":

#         # Get the symbol of the stock and number of shares the user want to buy from the HTML form
#         symbol = request.form.get("symbol")

#         # The 'type=int' argument would ensure if the form.get number is an int. If it isn't an int, it will return NoneType value
#         shares = request.form.get("shares", type=int)

#         # Query the database for the logged in user's cash
#         cash = db.execute("SELECT cash FROM users WHERE id=?", session["user_id"])

#         quote = lookup(symbol)

#         # Ensure that a symbol was submitted
#         if not symbol or symbol == " ":
#             return apology("Missing symbol")

#         # Check if the symbol is valid
#         elif quote == None:
#             return apology("Invalid symbol")

#         # Check if the shares is a positive number
#         elif not shares or shares <= 0:
#             return apology("Shares must be greater than or equal to one")

#         # Check if the user can afford the stock
#         elif cash[0]["cash"] < (quote["price"] * shares):
#             return apology("Not enough cash")

#         # Query the database for the number of shares the currently logged in user owns of the company
#         user_shares = db.execute("SELECT total_shares FROM stocks WHERE user_id=? AND symbol=?",
#                                  session["user_id"], quote["symbol"])

#         # Insert a new transaction of 'buy' to transactions table
#         db.execute("INSERT INTO transactions (symbol, shares, date_time, user_id, price, action) VALUES(?, ?, datetime('now', 'localtime'), ?, ?, 'Bought')",
#                    quote["symbol"], shares, session["user_id"], quote["price"])

#         # If user does not own any share, insert into the stocks table
#         if not user_shares:
#             db.execute("INSERT INTO stocks (symbol, total_shares, user_id) VALUES(?, ?, ?)",
#                        quote["symbol"], shares, session["user_id"])
#             cash[0]["cash"] -= (quote["price"] * shares)
#             db.execute("UPDATE users SET cash=? WHERE id=?", cash[0]["cash"], session["user_id"])
#             return redirect("/")

#         # If user does own a share, update their total shares in the stocks table
#         else:
#             user_shares[0]["total_shares"] += shares
#             db.execute("UPDATE stocks SET total_shares=? WHERE user_id=? AND symbol=?",
#                        user_shares[0]["total_shares"], session["user_id"], quote["symbol"])
#             cash[0]["cash"] -= (quote["price"] * shares)
#             db.execute("UPDATE users SET cash=? WHERE id=?", cash[0]["cash"], session["user_id"])

#         flash("Bought!")
#         return redirect("/")

#     else:
#         return render_template("buy.html")


# @app.route("/history")
# @login_required
# def history():
#     """Show history of transactions"""

#     # Query the database to get the list of all transactions done by the logged in user
#     transactions = db.execute(
#         "SELECT symbol, shares, date_time, price, action FROM transactions WHERE user_id=?", session["user_id"])

#     return render_template("history.html", transactions=transactions)


# @app.route("/login", methods=["GET", "POST"])
@app.route("/login")
def login():
#     """Log user in"""

#     # Forget any user_id
#     session.clear()

#     # User reached route via POST (as by submitting a form via POST)
#     if request.method == "POST":

#         # Ensure username was submitted
#         if not request.form.get("username"):
#             return apology("must provide username", 403)

#         # Ensure password was submitted
#         elif not request.form.get("password"):
#             return apology("must provide password", 403)

#         # Query database for username
#         rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

#         # Ensure username exists and password is correct
#         if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
#             flash("Register if you haven't already!", category="error")
#             return apology("invalid username and/or password", 403)

#         # Remember which user has logged in
#         session["user_id"] = rows[0]["id"]

#         flash("Login Successful!")
#         # Redirect user to home page
#         return redirect("/")

#     # User reached route via GET (as by clicking a link or via redirect)
#     else:
    return render_template("login.html")


# @app.route("/logout")
# def logout():
#     """Log user out"""

#     # Forget any user_id
#     session.clear()

#     # Redirect user to login form
#     return redirect("/")


# @app.route("/quote", methods=["GET", "POST"])
# @login_required
# def quote():
#     """Get stock quote."""

#     if request.method == "POST":

#         # Get the symbol from the HTML form and check it's validity
#         symbol = request.form.get("symbol")

#         quote = lookup(symbol)

#         # Return an apology if symbol is not valid
#         if quote == None:
#             return apology("Invalid symbol")

#         # If symbol is valid, return it's stock price
#         return render_template("quoted.html", name=quote["name"], price=usd(quote["price"]), symbol=quote["symbol"])
#     else:
#         return render_template("quote.html")


# @app.route("/register", methods=["GET", "POST"])
# def register():
#     """Register user"""

#     if request.method == "POST":

#         # Get the username, password and confirmation password from the HTML form.
#         username = request.form.get("username")
#         password = request.form.get("password")
#         confirm_pass = request.form.get("confirmation")

#         # Query the database to get the list of all users.
#         users = db.execute("SELECT * FROM users")

#         # Check if the username was submitted.
#         if not username or username == ' ':
#             return apology("Username cannot be blank")

#         # Check if the username already exists.
#         for user in users:
#             if username == user["username"]:
#                 return apology("Username already exists")

#         # Ensure that passwords were submitted.
#         if not password or not confirm_pass:
#             return apology("Password cannot be blank")

#         # Ensure that the password and confirmation password match.
#         elif password != confirm_pass:
#             return apology("Passwords do not match")

#         # Register the user.
#         db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, generate_password_hash(password))

#         # Query the database to get the id of the user.
#         user = db.execute("SELECT id FROM users WHERE username=?", username)

#         # Remember the id of the logged in user.
#         session["user_id"] = user[0]["id"]

#         flash("Registration Successful!")
#         return redirect("/")

#     else:
#         return render_template("register.html")


# @app.route("/sell", methods=["GET", "POST"])
# @login_required
# def sell():
#     """Sell shares of stock"""

#     if request.method == "POST":

#         # Get the symbol and the number of shares user want to sell from the HTML form
#         symbol = request.form.get("symbol")
#         shares = request.form.get("shares", type=int)

#         # Query the database for amount of cash user has
#         cash = db.execute("SELECT cash FROM users WHERE id=?", session["user_id"])
#         user_cash = cash[0]["cash"]

#         # Query the database for the number of shares the user owns
#         user_stocks = db.execute("SELECT total_shares FROM stocks WHERE user_id=? AND symbol=?", session["user_id"], symbol)

#         # Check if the symbol submitted is vaild
#         if not user_stocks:
#             return apology("Invalid symbol")

#         # Ensure that the number of shares submitted are greater than zero
#         elif not shares or shares <= 0:
#             return apology("Shares must be greater than or equal to one")

#         # Ensure that the user is selling appropriate number of shares
#         elif shares > user_stocks[0]["total_shares"]:
#             return apology("Cannot sell more shares than owned")

#         # Lookup the current prices of the stock
#         quote = lookup(symbol)
#         user_cash += (quote["price"] * shares)

#         # Update the number of shares user owns after selling
#         user_stocks[0]["total_shares"] -= shares

#         # Insert a new transaction of 'sell' to the transactions table
#         db.execute("INSERT INTO transactions (symbol, shares, date_time, user_id, price, action) VALUES(?, ?, datetime('now', 'localtime'), ?, ?, 'Sold')",
#                    symbol, shares, session["user_id"], quote["price"])

#         # If user sold all their shares, delete the stock from their portfolio and update their cash
#         if user_stocks[0]["total_shares"] == 0:
#             db.execute("DELETE FROM stocks WHERE user_id=? AND symbol=?", session["user_id"], symbol)
#             db.execute("UPDATE users SET cash=? WHERE id=?", user_cash, session["user_id"])

#         # If user did not sell all the shares, update the number of shares user is left with after selling and update their cash
#         else:
#             db.execute("UPDATE stocks SET total_shares=? WHERE user_id=? AND symbol=?",
#                        user_stocks[0]["total_shares"], session["user_id"], symbol)
#             db.execute("UPDATE users SET cash=? WHERE id=?", user_cash, session["user_id"])

#         flash("Sold!")
#         return redirect("/")

#     else:
#         user_stocks = db.execute("SELECT symbol, total_shares FROM stocks WHERE user_id=?", session["user_id"])

#         return render_template("sell.html", user_stocks=user_stocks)


# @app.route("/profile", methods=["GET", "POST"])
# @login_required
# def profile():
#     """SHOW USER PROFILE"""

#     if request.method == "POST":

#         old_pass = request.form.get("old_pass")
#         new_pass = request.form.get("new_pass")
#         confirm_pass = request.form.get("confirm_pass")

#         user = db.execute("SELECT username, hash FROM users WHERE id = ?", session["user_id"])

#         if not old_pass or old_pass == " ":
#             return apology("Old password field is blank.")

#         elif not check_password_hash(user[0]["hash"], old_pass):
#             return apology("Old password is wrong!")

#         elif not new_pass or not confirm_pass or new_pass == " " or confirm_pass == " ":
#             return apology("New password field is blank")

#         elif new_pass != confirm_pass:
#             return apology("Confirmation password does not match with new password.")

#         elif check_password_hash(user[0]["hash"], new_pass):
#             return apology("New password cannot be same as the old password.")

#         db.execute("UPDATE users SET hash=? WHERE id=?", generate_password_hash(new_pass), session["user_id"])

#         flash("Password Updated!")

#         return redirect("/")

#     else:
#         user = db.execute("SELECT username, hash FROM users WHERE id = ?", session["user_id"])
#         return render_template("profile.html", user=user[0]["username"])


# @app.route("/delete", methods=["POST"])
# @login_required
# def delete():
#     if request.method == "POST":

#         user = request.form.get("delete")

#         db.execute("DELETE FROM stocks WHERE user_id=?", session["user_id"])

#         db.execute("DELETE FROM transactions WHERE user_id=?", session["user_id"])

#         db.execute("DELETE FROM users WHERE id=?", session["user_id"])

#         flash("Account Deleted!")

#         return redirect("/login")


# @app.route("/cash", methods=["POST"])
# @login_required
# def add_cash():

#     amount = request.form.get("amount", type=float)

#     if not amount or amount == " ":
#         flash("Amount to be added not specified", category="error")
#         return redirect("/profile")

#     elif amount < 1:
#         flash("Cash to be added cannot be a negative value or 0!", category="error")
#         return redirect("/profile")

#     elif amount > 5000:
#         flash("You cannot add more than $5000 at once!", category="error")
#         return redirect("/profile")

#     user_cash = db.execute("SELECT cash FROM users WHERE id=?", session["user_id"])

#     user_cash[0]["cash"] += amount

#     db.execute("UPDATE users SET cash=? WHERE id=?", user_cash[0]["cash"], session["user_id"])

#     flash("Cash added successfully!")

#     return redirect("/")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
