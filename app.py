from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage
check_ins = []

# Home page
@app.route("/")
def home():
    return render_template("home.html")

# Check-in page
@app.route("/checkin", methods=["GET", "POST"])  #form to submit
def checkin():
    if request.method == "POST":
        mood = request.form.get("mood")
        task = request.form.get("task")
        brave = request.form.get("brave")
        check_ins.append({"mood": mood, "task": task, "brave": brave})
        return redirect(url_for("progress"))
    return render_template("checkin.html")

# Progress page
@app.route("/progress")    #shows list of past submission and total check-ins
def progress():
    total_checkins = len(check_ins)
    return render_template("progress.html", check_ins=check_ins, total=total_checkins)

if __name__ == "__main__":
    app.run(debug=True)