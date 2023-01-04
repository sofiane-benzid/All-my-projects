from flask import Flask , redirect, render_template, session, request, flash, url_for
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required
import math
import datetime


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db = SQL("sqlite:///gym.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("layout.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "GET":
        return render_template("login.html")
    else:
        if not request.form.get("username"):
            flash ("Username field required","warning")
            return render_template("login.html")
        if not request.form.get("password"):
            flash ("Password required")
            return render_template("login.html")
        row = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if len(row) != 1 or not check_password_hash(row[0]["hash"], request.form.get("password")):
            flash ("invalid username and/or password")
            return render_template("login.html")

        session["user_id"] = row[0]["id"]
        return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        verify_password = request.form.get("verify_password")
        username_check = db.execute("SELECT * FROM users WHERE username=?", username)

        if username_check:
            flash("Username already taken")
            return render_template("register.html")
        if not username:
            flash("Username field is required")
            return render_template("register.html")
        if not password:
            flash("Password field is required")
            return render_template("register.html")
        if not verify_password:
            flash("Verify password field is required")
            return render_template("register.html")
        if password != verify_password:
            flash("Passwords do not match")
            return render_template("register.html")
        pw_hash = generate_password_hash(password)
        new_user = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, pw_hash)
        session["user_id"] = new_user
        return redirect("/")
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/calculators", methods=["GET", "POST"])
@login_required

def calculator():
    if request.method == "GET":
        return render_template ("calculator.html")
    if request.method == "POST":
        if request.form['submit_button'] == 'Body fat calculator':
            bodyfat= True
            return render_template("calculator.html", bodyfat=bodyfat)
        if request.form['submit_button'] == 'Calories burned calculator':
            calories= True
            return render_template("calculator.html", calories=calories)
        if request.form['submit_button'] == 'Ideal weight calculator':
            ideal= True
            return render_template("calculator.html", ideal=ideal)
        if request.form['submit_button'] == 'Protein calculator':
            protein= True
            return render_template("calculator.html", protein=protein)

        return render_template("calculator.html")

@app.route("/bodyfat", methods=["GET", "POST"])
@login_required

def bodyfat():
    height = request.form.get("height")
    sex = request.form.get("sex")
    neck = request.form.get("neck")
    waist = request.form.get("waist")
    if not height or not neck or not waist:
        flash("All fields required")
    if sex == 'Male':
        if height and neck and waist:
            height = float(height)
            neck = float(neck)
            waist = float(waist)
            result = (495 / (1.0324 - 0.19077*math.log(waist-neck, 10) + 0.15456*math.log(height, 10))) - 450

            bodyfatresult = True
            return render_template("calculator.html", result=round(result), bodyfatresult=bodyfatresult, sex=sex)
    if sex == 'Female':
        if height and neck and waist:
            height = float(height)
            neck = float(neck)
            waist = float(waist)
            result = (495 / (1.29579 - 0.35004*math.log(waist+102-neck, 10) + 0.22100*math.log(height, 10))) - 450
            bodyfatresult = True
            return render_template("calculator.html", result=round(result), bodyfatresult=bodyfatresult, sex=sex)
    return render_template("calculator.html")

@app.route("/calories", methods=["POST", "GET"])
@login_required
def calories():
    height = request.form.get("height")
    sex = request.form.get("sex")
    age = request.form.get("age")
    weight = request.form.get("weight")
    activity = request.form.get("activity")
    if not height or not age or not weight or not activity:
        flash("All fields required")
    if sex == 'Male':
        if height and weight and age and activity:
            height = int(height)
            weight = int(weight)
            age = int(age)
            calorieresult = True
            if activity == '1':
                result = (10*weight + 6.25*height - 5*age + 5)* 1.2
            elif activity == '2':
                result = (10*weight + 6.25*height - 5*age + 5)* 1.37
            elif activity == '3':
                result = (10*weight + 6.25*height - 5*age + 5)* 1.45
            return render_template("calculator.html", calorieresult=calorieresult, result=round(result))
    if sex == 'Female':
        if height and weight and age and activity:
            height = int(height)
            weight = int(weight)
            age = int(age)
            calorieresult = True
            if activity == '1':
                result = (10*weight + 6.25*height - 5*age - 161)* 1.2
            elif activity == '2':
                result = (10*weight + 6.25*height - 5*age - 161)* 1.37
            elif activity == '3':
                result = (10*weight + 6.25*height - 5*age - 161)* 1.45
            return render_template("calculator.html", calorieresult=calorieresult, result=round(result))
    return render_template("calculator.html")

@app.route("/protein", methods=["POST", "GET"])
@login_required
def protein():
    height = request.form.get("height")
    sex = request.form.get("sex")
    age = request.form.get("age")
    weight = request.form.get("weight")
    activity = request.form.get("activity")
    if not height or not age or not weight or not activity:
        flash("All fields required")
    if sex == 'Male':
        if height and weight and age and activity:
            height = int(height)
            weight = int(weight)
            age = int(age)
            proteinresult = True
            if activity == '1':
                result = (((10*weight + 6.25*height - 5*age + 5)* 1.2) * 0.4)/4
            elif activity == '2':
                result = (((10*weight + 6.25*height - 5*age + 5)* 1.37) *0.4)/4
            elif activity == '3':
                result = (((10*weight + 6.25*height - 5*age + 5)* 1.45) *0.4)/4
            return render_template("calculator.html", proteinresult=proteinresult, result=round(result))
    if sex == 'Female':
        if height and weight and age and activity:
            height = int(height)
            weight = int(weight)
            age = int(age)
            proteinresult = True
            if activity == '1':
                result = (((10*weight + 6.25*height - 5*age - 161)* 1.2) *0.4)/4
            elif activity == '2':
                result = (((10*weight + 6.25*height - 5*age - 161)* 1.37)*0.4)/4
            elif activity == '3':
                result = (((10*weight + 6.25*height - 5*age - 161)* 1.45)*0.4)/4
            return render_template("calculator.html", proteinresult=proteinresult, result=round(result))
    return render_template("calculator.html")


@app.route("/workouts", methods=["POST", "GET"])
@login_required

def workouts():
    if request.method == "GET":
        check = db.execute("SELECT * FROM workouts WHERE user_id=?", session["user_id"])
        if len(check) == 0:
            return render_template("addworkout.html")
        i_sunday = db.execute("SELECT sunday FROM workouts WHERE user_id=?", session["user_id"])
        i_monday = db.execute("SELECT monday FROM workouts")
        i_tuesday = db.execute("SELECT tuesday FROM workouts")
        i_wednesday = db.execute("SELECT wednesday FROM workouts")
        i_thursday = db.execute("SELECT thursday FROM workouts")
        i_friday = db.execute("SELECT friday FROM workouts")
        i_saturday = db.execute("SELECT saturday FROM workouts")
        return render_template("workouts.html", i_saturday=i_saturday , i_sunday=i_sunday, i_monday=i_monday, i_tuesday=i_tuesday,i_wednesday=i_wednesday,i_thursday=i_thursday,i_friday=i_friday)
    else:
        name = request.form.get("name")
        sunday = request.form.get("sunday")
        monday = request.form.get("monday")
        tuesday = request.form.get("tuesday")
        wednesday = request.form.get("wednesday")
        thursday = request.form.get("thursday")
        friday = request.form.get("friday")
        saturday = request.form.get("saturday")
        if not (name or sunday or monday or tuesday or wednesday or thursday or friday or saturday):
            flash ("All fields required")
            return render_template("addworkout.html")
        db.execute("INSERT INTO workouts(user_id, workout_name, sunday, monday, tuesday, wednesday, thursday, friday, saturday) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", session["user_id"], name, sunday, monday, tuesday, wednesday, thursday, friday, saturday)

        return redirect('/workouts')

@app.route("/deleteworkout", methods=["POST", "GET"])
@login_required

def deleteworkout():
    db.execute("DELETE FROM workouts WHERE user_id=?", session["user_id"])
    db.execute("DELETE FROM exercises WHERE user_id=?", session["user_id"])
    return redirect("/workouts")

@app.route("/editworkout", methods=["POST"])
@login_required

def editworkout():
    if request.method == "POST":
        button = request.form.get("edit")
        if button == 'saturday':
            day = db.execute("SELECT saturday FROM workouts WHERE user_id=?",session["user_id"])
            return render_template("editworkout.html", day=day[0]['saturday'], saturday='Saturday')
        if button == 'sunday':
            day = db.execute("SELECT sunday FROM workouts WHERE user_id=?",session["user_id"])
            return render_template("editworkout.html", day=day[0]['sunday'], saturday='Sunday')
        if button == 'monday':
            day = db.execute("SELECT monday FROM workouts WHERE user_id=?",session["user_id"])
            return render_template("editworkout.html", day=day[0]['monday'], saturday='Monday')
        if button == 'tuesday':
            day = db.execute("SELECT tuesday FROM workouts WHERE user_id=?",session["user_id"])
            return render_template("editworkout.html", day=day[0]['tuesday'], saturday='Tuesday')
        if button == 'wednesday':
            day = db.execute("SELECT wednesday FROM workouts WHERE user_id=?",session["user_id"])
            return render_template("editworkout.html", day=day[0]['wednesday'], saturday='Wednesday')
        if button == 'thursday':
            day = db.execute("SELECT thursday FROM workouts WHERE user_id=?",session["user_id"])
            return render_template("editworkout.html", day=day[0]['thursday'], saturday='Thursday')
        if button == 'friday':
            day = db.execute("SELECT friday FROM workouts WHERE user_id=?",session["user_id"])
            return render_template("editworkout.html", day=day[0]['friday'], saturday='friday')

        return render_template("editworkout.html")

@app.route("/edited", methods=["POST"])
@login_required

def edited():
    button = request.form.get("edit")
    edit = request.form.get("newedit")
    if button == 'Saturday':
        db.execute("UPDATE workouts SET saturday = ? WHERE user_id=?",edit, session["user_id"])
        return redirect("/workouts")
    if button == 'Sunday':
        db.execute("UPDATE workouts SET sunday = ? WHERE user_id=?",edit, session["user_id"])
        return redirect("/workouts")
    if button == 'Monday':
        db.execute("UPDATE workouts SET monday = ? WHERE user_id=?",edit, session["user_id"])
        return redirect("/workouts")
    if button == 'Tuesday':
        db.execute("UPDATE workouts SET tuesday = ? WHERE user_id=?",edit, session["user_id"])
        return redirect("/workouts")
    if button == 'Wednesday':
        db.execute("UPDATE workouts SET wednesday = ? WHERE user_id=?",edit, session["user_id"])
        return redirect("/workouts")
    if button == 'Thursday':
        db.execute("UPDATE workouts SET thursday = ? WHERE user_id=?",edit, session["user_id"])
        return redirect("/workouts")
    if button == 'Friday':
        db.execute("UPDATE workouts SET friday = ? WHERE user_id=?",edit, session["user_id"])
        return redirect("/workouts")

@app.route("/workouts/<day>", methods=["POST", "GET"])
@login_required

def exercise(day):
    if request.method == "GET":
        info = db.execute("SELECT * FROM exercises WHERE user_id=? AND day=?",session["user_id"],day)
        return render_template("lol.html", info= info, day=day.capitalize())
    else:
        info = db.execute("SELECT * FROM exercises WHERE user_id=? AND day=?",session["user_id"],day)
        return render_template("lol.html", info=info, day=day.capitalize())

@app.route("/addexercise", methods=["POST","GET"])
@login_required

def addexercise():
    if request.method=="GET":
        return render_template("addexercise.html")
    else:
        name = request.form.get("name")
        muscles = request.form.get("muscles")
        if not name or not muscles:
            flash("All fields required")
            return redirect("/addexercise")
        saturday = request.form.get("Saturday")
        sunday = request.form.get("Sunday")
        monday = request.form.get("Monday")
        tuesday = request.form.get("Tuesday")
        wednesday = request.form.get("Wednesday")
        thursday = request.form.get("Thursday")
        friday = request.form.get("Friday")
        if saturday:
            db.execute("INSERT INTO exercises (user_id, day, name, muscles) VALUES (?, ?, ?, ?)", session["user_id"],'saturday',name, muscles)
            return redirect("/workouts/saturday")
        if sunday:
            db.execute("INSERT INTO exercises (user_id, day, name, muscles) VALUES (?, ?, ?, ?)", session["user_id"],'sunday',name, muscles)
            return redirect("/workouts/sunday")
        if monday:
            db.execute("INSERT INTO exercises (user_id, day, name, muscles) VALUES (?, ?, ?, ?)", session["user_id"],'monday',name, muscles)
            return redirect("/workouts/monday")
        if tuesday:
            db.execute("INSERT INTO exercises (user_id, day, name, muscles) VALUES (?, ?, ?, ?)", session["user_id"],'tuesday',name, muscles)
            return redirect("/workouts/tuesday")
        if wednesday:
            db.execute("INSERT INTO exercises (user_id, day, name, muscles) VALUES (?, ?, ?, ?)", session["user_id"],'wednesday',name, muscles)
            return redirect("/workouts/wednesday")
        if thursday:
            db.execute("INSERT INTO exercises (user_id, day, name, muscles) VALUES (?, ?, ?, ?)", session["user_id"],'thursday',name, muscles)
            return redirect("/workouts/thursday")
        if friday:
            db.execute("INSERT INTO exercises (user_id, day, name, muscles) VALUES (?, ?, ?, ?)", session["user_id"],'friday',name, muscles)
            return redirect("/workouts/friday")




@app.route("/placeholder", methods=["POST"])
@login_required

def placeholder():
    saturday = request.form.get("Saturday")
    sunday = request.form.get("Sunday")
    monday = request.form.get("Monday")
    tuesday = request.form.get("Tuesday")
    wednesday = request.form.get("Wednesday")
    thursday = request.form.get("Thursday")
    friday = request.form.get("Friday")

    if saturday:
        return render_template("addexercise.html", day = 'Saturday')
    if sunday:
        return render_template("addexercise.html", day = 'Sunday')
    if monday:
        return render_template("addexercise.html", day = 'Monday')
    if tuesday:
        return render_template("addexercise.html", day = 'Tuesday')
    if wednesday:
        return render_template("addexercise.html", day = 'Wednesday')
    if thursday:
        return render_template("addexercise.html", day = 'Thursday')
    if friday:
        return render_template("addexercise.html", day = 'Friday')
    return render_template("addexercise.html", day ='Your mom')

@app.route("/deleteexercise", methods=["POST"])
@login_required

def deleteexercise():
    saturday = request.form.get("Saturday")
    sunday = request.form.get("Sunday")
    monday = request.form.get("Monday")
    tuesday = request.form.get("Tuesday")
    wednesday = request.form.get("Wednesday")
    thursday = request.form.get("Thursday")
    friday = request.form.get("Friday")
    if saturday:
        db.execute("DELETE FROM exercises WHERE user_id=? AND id=?",session["user_id"], saturday)
        return redirect("/workouts/saturday")
    if sunday:
        db.execute("DELETE FROM exercises WHERE user_id=? AND id=?",session["user_id"], sunday)
        return redirect("/workouts/sunday")
    if monday:
        db.execute("DELETE FROM exercises WHERE user_id=? AND id=?",session["user_id"], monday)
        return redirect("/workouts/monday")
    if tuesday:
        db.execute("DELETE FROM exercises WHERE user_id=? AND id=?",session["user_id"], tuesday)
        return redirect("/workouts/tuesday")
    if wednesday:
        db.execute("DELETE FROM exercises WHERE user_id=? AND id=?",session["user_id"], wednesday)
        return redirect("/workouts/wednesday")
    if thursday:
        db.execute("DELETE FROM exercises WHERE user_id=? AND id=?",session["user_id"], thursday)
        return redirect("/workouts/thursday")
    if friday:
        db.execute("DELETE FROM exercises WHERE user_id=? AND id=?",session["user_id"], friday)
        return redirect("/workouts/friday")

@app.route("/setsreps", methods=["POST"])
@login_required

def setsreps():
    saturday = request.form.get("Saturday")
    sunday = request.form.get("Sunday")
    monday = request.form.get("Monday")
    tuesday = request.form.get("Tuesday")
    wednesday = request.form.get("Wednesday")
    thursday = request.form.get("Thursday")
    friday = request.form.get("Friday")
    sets = request.form.get("sets")
    reps = request.form.get("reps")
    weight = request.form.get("weight")
    if not sets or not reps or not weight:
        flash("All fields required")
        return redirect("/workouts")
    date = datetime.datetime.now()
    if saturday:
        db.execute("INSERT INTO setsreps (user_id, exercise_id, day, sets, reps, weight, date) VALUES (?, ?, ?, ?, ?, ?, ?)",session["user_id"], saturday, 'saturday', sets, reps, weight, date)
        return redirect("/workouts/saturday")
    if sunday:
        db.execute("INSERT INTO setsreps (user_id, exercise_id, day, sets, reps, weight, date) VALUES (?, ?, ?, ?, ?, ?, ?)",session["user_id"], sunday, 'sunday', sets, reps, weight, date)
        return redirect("/workouts/sunday")
    if monday:
        db.execute("INSERT INTO setsreps (user_id, exercise_id, day, sets, reps, weight, date) VALUES (?, ?, ?, ?, ?, ?, ?)",session["user_id"], monday, 'monday', sets, reps, weight, date)
        return redirect("/workouts/monday")
    if tuesday:
        db.execute("INSERT INTO setsreps (user_id, exercise_id, day, sets, reps, weight, date) VALUES (?, ?, ?, ?, ?, ?, ?)",session["user_id"], tuesday, 'tuesday', sets, reps, weight, date)
        return redirect("/workouts/tuesday")
    if wednesday:
        db.execute("INSERT INTO setsreps (user_id, exercise_id, day, sets, reps, weight, date) VALUES (?, ?, ?, ?, ?, ?, ?)",session["user_id"], wednesday, 'wednesday', sets, reps, weight, date)
        return redirect("/workouts/wednesday")
    if thursday:
        db.execute("INSERT INTO setsreps (user_id, exercise_id, day, sets, reps, weight, date) VALUES (?, ?, ?, ?, ?, ?, ?)",session["user_id"], thursday, 'thursday', sets, reps, weight, date)
        return redirect("/workouts/thursday")
    if friday:
        db.execute("INSERT INTO setsreps (user_id, exercise_id, day, sets, reps, weight, date) VALUES (?, ?, ?, ?, ?, ?, ?)",session["user_id"], friday, 'friday', sets, reps, weight, date)
        return redirect("/workouts/friday")

@app.route("/graphs", methods=["POST", "GET"])
@login_required

def graphs():
    if request.method == "GET":
        info = db.execute("SELECT name FROM exercises WHERE id IN (SELECT exercise_id FROM setsreps WHERE user_id=?)",session['user_id'])
        return render_template("graphs.html", info=info)
    if request.method == "POST":
        name = request.form.get("exercise")
        if not name:
            flash("Please choose an exercise")
            return redirect("/graphs")
        sets = db.execute("SELECT sets FROM setsreps WHERE exercise_id IN (SELECT id FROM exercises WHERE name = ? AND user_id=?)", name, session['user_id'])
        reps = db.execute("SELECT reps FROM setsreps WHERE exercise_id IN (SELECT id FROM exercises WHERE name = ? AND user_id=?)", name, session['user_id'])
        weight = db.execute("SELECT weight FROM setsreps WHERE exercise_id IN (SELECT id FROM exercises WHERE name = ? AND user_id=?)", name, session['user_id'])
        date = db.execute("SELECT date FROM setsreps WHERE exercise_id IN (SELECT id FROM exercises WHERE name = ? AND user_id=?)", name, session['user_id'])
        set_list =[]
        rep_list =[]
        weight_list =[]
        total_list = []
        date_list = []
        for x in weight:
            weight_list.append(x['weight'])
        for x in sets:
            set_list.append(x['sets'])
        for x in reps:
            rep_list.append(x['reps'])
        for x in date:
            date_list.append(x['date'])

        for i in range (len(weight_list)):
            total = 0
            total = weight_list[i] * set_list[i] * rep_list[i]
            total_list.append(total)

        labels = total_list
        values = date_list
        for y in date_list:
            print(y)

        return render_template ("graph.html", labels=labels, values=values)


if __name__ == '__main__':
    app.run(debug=True)