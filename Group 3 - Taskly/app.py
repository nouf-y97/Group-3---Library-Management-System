from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("dashboard"))
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")

@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    return render_template("forgot_password.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/tasks")
def tasks():
    return render_template("tasks.html")

@app.route("/add-task")
def add_task():
    return render_template("add_task.html")

@app.route("/edit-task/<int:task_id>")
def edit_task(task_id):
    return render_template("edit_task.html")

@app.route("/task-details/<int:task_id>")
def task_details(task_id):
    return render_template("task_details.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

if __name__ == "__main__":
    app.run(debug=True)