from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "taskly-secret-key"
DATABASE = "taskly.db"


# ================= DATABASE CONNECTION =================

def get_db():
    conn = sqlite3.connect("taskly.db")
    conn.row_factory = sqlite3.Row
    return conn
from werkzeug.security import generate_password_hash
import sqlite3

conn = sqlite3.connect("taskly.db")

users = [
    ("Nouf", "123456"),
    ("Sara", "654321"),
    ("Ali", "789123"),
    ("Ahmed", "111111"),
    ("Dalal", "222222"),
    ("Fahad", "333333"),
    ("Reem", "444444"),
    ("Khalid", "555555"),
    ("Nora", "666666"),
    ("Afnan", "777777")
]

for username, password in users:
    hashed_password = generate_password_hash(password)

    conn.execute(
        "UPDATE users SET password = ? WHERE username = ?",
        (hashed_password, username)
    )

conn.commit()
conn.close()

print("Passwords updated successfully!")

print("Passwords updated successfully!")
# ================= AUTH ROUTES =================

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            return redirect(url_for("dashboard"))

        return "Username or password is wrong"

    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
    
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        conn = get_db()

        try:
            conn.execute("""
            INSERT INTO users ( email, username, password)
            VALUES (?, ?, ?)
            """, ( email, username, hashed_password))

            conn.commit()

        except sqlite3.IntegrityError:
            conn.close()
            return "Email or username already exists"

        conn.close()
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    return render_template("forgot_password.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# ================= PAGES ROUTES =================

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db()

    total_tasks = conn.execute(
        "SELECT COUNT(*) FROM tasks WHERE user_id = ?",
        (session["user_id"],)
    ).fetchone()[0]

    completed_tasks = conn.execute(
        "SELECT COUNT(*) FROM tasks WHERE user_id = ? AND status = ?",
        (session["user_id"], "Completed")
    ).fetchone()[0]

    pending_tasks = conn.execute(
        "SELECT COUNT(*) FROM tasks WHERE user_id = ? AND status = ?",
        (session["user_id"], "Pending")
    ).fetchone()[0]

    conn.close()

    return render_template(
        "dashboard.html",
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        pending_tasks=pending_tasks
    )


@app.route("/tasks")
def tasks():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    tasks = conn.execute(
        "SELECT * FROM tasks WHERE user_id = ?",
        (session["user_id"],)
    ).fetchall()
    conn.close()

    return render_template("tasks.html", tasks=tasks)


@app.route("/add-task", methods=["GET", "POST"])
def add_task():
    

    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        priority = request.form["priority"]
        due_date = request.form["due_date"]

        conn = get_db()

        category = conn.execute(
            "SELECT id FROM categories WHERE user_id = ? LIMIT 1",
            (session["user_id"],)
        ).fetchone()

        category_id = category["user_id"] if category else None

        conn.execute("""
        INSERT INTO tasks (title, description, priority, due_date, status, category_id, user_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            title,
            description,
            priority,
            due_date,
            "Pending",
            category_id,
            session["user_id"]
        ))

        conn.commit()
        conn.close()

        return redirect(url_for("tasks"))

    return render_template("add_task.html")


@app.route("/task-details/<int:task_id>")
def task_details(task_id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ? AND user_id = ?",
        (task_id, session["user_id"])
    ).fetchone()
    conn.close()

    if task is None:
        return "Task not found"

    return render_template("task_details.html", task=task)


@app.route("/edit-task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db()

    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ? AND user_id = ?",
        (task_id, session["user_id"])
    ).fetchone()

    if task is None:
        conn.close()
        return "Task not found"

    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        priority = request.form["priority"]
        due_date = request.form["due_date"]

        conn.execute("""
        UPDATE tasks
        SET title = ?, description = ?, priority = ?, due_date = ?
        WHERE id = ? AND user_id = ?
        """, (
            title,
            description,
            priority,
            due_date,
            task_id,
            session["user_id"]
        ))

        conn.commit()
        conn.close()

        return redirect(url_for("task_details", task_id=task_id))

    conn.close()
    return render_template("edit_task.html", task=task)


@app.route("/delete-task/<int:task_id>")
def delete_task(task_id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    conn.execute(
        "DELETE FROM tasks WHERE id = ? AND user_id = ?",
        (task_id, session["user_id"])
    )
    conn.commit()
    conn.close()

    return redirect(url_for("tasks"))


@app.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    user = conn.execute(
        "SELECT * FROM users WHERE id = ?",
        (session["user_id"],)
    ).fetchone()
    conn.close()

    return render_template("profile.html", user=user)


# ================= RUN APP =================

if __name__ == "__main__":
    app.run(debug=True)