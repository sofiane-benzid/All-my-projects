import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user = session["user_id"]
    cash = db.execute("SELECT cash FROM users WHERE id =?", user)
    symbols = db.execute("SELECT symbol FROM buys WHERE user_id=?", user)


    symbol_lst =[]
    share_lst = []
    price_lst =[]
    name_lst =[]
    for symbol in symbols:
        if symbol["symbol"] not in symbol_lst:
            symbol_lst.append(symbol["symbol"])
    i=0
    for z in symbol_lst:
        shares = db.execute("SELECT SUM(shares) as shares FROM buys WHERE symbol =? and user_id =?", z, session["user_id"])
        share_sum=0
        for share in shares:
            share_sum += share["shares"]
        share_lst.append(share_sum)
        tmp_lookup = lookup(z)
        name_lst.append(tmp_lookup["name"])
        price_one = tmp_lookup["price"] * share_lst[i]
        i+=1
        price_lst.append(price_one)

    total = cash[0]["cash"]
    for i in range(len(price_lst)):
        total+=price_lst[i]


    length = len(symbol_lst) + 1
    return render_template("index.html",share_lst=share_lst, price_lst=price_lst ,name_lst=name_lst, length=length, cash=cash, total=total)



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stck"""
    if request.method == "GET":
        return render_template("buy.html")
    else:
        number = request.form.get("number")
        symbol = request.form.get("symbol").upper()
        stock = lookup(symbol)
        if not number:
            return apology("Number of stocks field required")
        if not symbol:
            return apology("Stock symbol field is required")
        if not stock:
            return apology ("Stock symbol does not exist")

        shares = int(number)
        if shares < 1:
            return apology("Number of stocks must be positive")
        user = session["user_id"]
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user)
        tx_price = stock["price"] * shares
        if tx_price > cash[0]["cash"]:
            return apology("You do not have enough cash to perform this transactions")
        new_cash = cash[0]["cash"] - tx_price
        date= datetime.datetime.now()
        db_tx = db.execute("SELECT symbol FROM buys WHERE user_id = ?", session["user_id"])
        db.execute("UPDATE users SET cash = ? WHERE id = ?",new_cash, user)
        ex_shares = db.execute("SELECT shares FROM buys WHERE user_id = ? and symbol = ?", session["user_id"], stock["symbol"])
        if {'symbol': symbol} in db_tx:
            nm_shares = shares + ex_shares[0]["shares"]
            db.execute("UPDATE buys SET shares = ? WHERE user_id = ? and symbol = ? ", nm_shares, session["user_id"], symbol)
        else:
            db.execute("INSERT INTO buys (user_id, symbol, shares, price, date) VALUES (?, ?, ?, ?, ?)", user , stock["symbol"] ,shares , stock["price"], date)
        db.execute("INSERT INTO history(user_id, symbol, shares, price, date, type) VALUES (?, ?, ?, ?, ?, ?)", user, stock["symbol"],shares,stock["price"],date, 'BUY')
        flash("Buy successful")
        return redirect("/")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    history = db.execute("SELECT * FROM history;")
    return render_template("history.html", history=history)



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template('quote.html')

    else:
        symbol = request.form.get("quote")
        stock = lookup(symbol)
        if not stock:
            return apology("Stock symbol does not exist")
        name = stock["name"]
        sb = stock["symbol"]
        price = usd(stock["price"])
        return render_template('quoted.html', name=name, price=price)




@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template('register.html')
    else:
        name = request.form.get("username")
        password = request.form.get("password")
        verify_password = request.form.get("verify_password")
        user_name = db.execute("SELECT * FROM users WHERE username=?", name)
        if not name:
            return apology("Name field is required")
        if not password:
            return apology("Password required")
        if not verify_password:
            return apology("Password verification required")
        if password != verify_password:
            return apology("Password and confirmation do not match")
        if user_name:
            return apology("Username is already taken")
        pw_hash = generate_password_hash(password)
        new_user = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", name, pw_hash)
        session["user_id"] = new_user
        return redirect("/")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        symbols = db.execute("SELECT symbol FROM buys WHERE user_id = ?", session["user_id"])
        symbol_lst= []
        for symbol in symbols:
            if symbol["symbol"] not in symbol_lst:
                symbol_lst.append(symbol["symbol"])
        return render_template("sell.html", symbols=symbol_lst)
    else:
        number = request.form.get("number")
        symbol = request.form.get("symbol")
        stock = lookup(symbol)
        owned_shares = db.execute("SELECT SUM(shares) AS shares FROM buys WHERE symbol=? AND user_id =?",symbol, session["user_id"])
        if not number:
            return apology("Number of stocks field required")
        if not symbol:
            return apology("Stock symbol field is required")

        shares = int(number)
        if shares < 1:
            return apology("Number of stocks must be positive")
        if owned_shares[0]["shares"] < shares:
            return apology("You do not have that amount of shares")
        user = session["user_id"]
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user)
        tx_price = stock["price"] * shares
        new_cash = cash[0]["cash"] + tx_price
        date= datetime.datetime.now()
        db.execute("UPDATE users SET cash = ? WHERE id = ?",new_cash, user)
        if owned_shares[0]["shares"] == shares:
            db.execute("DELETE FROM buys WHERE user_id= ? AND symbol= ?", session["user_id"], stock["symbol"])
        new_shares = owned_shares[0]["shares"] - shares
        if owned_shares[0]["shares"] > shares:
            db.execute("UPDATE buys SET shares = ? WHERE user_id = ? and symbol = ?", new_shares, session["user_id"], stock["symbol"])
        date = datetime.datetime.now()
        db.execute("INSERT INTO history(user_id, symbol, shares, price, date, type) VALUES (?, ?, ?, ?, ?, ?)", session["user_id"], stock["symbol"],shares,stock["price"],date, 'SELL')
        flash("Sell successful")
        return redirect("/")

