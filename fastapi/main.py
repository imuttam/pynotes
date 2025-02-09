from flask import Flask, render_template, session, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for session tracking

# Reset session on startup
@app.before_request
def before_request():
    if "todo_id" not in session:
        session["todo_id"] = 1

@app.route("/")
def home():
    return redirect(url_for("get_todo"))

@app.route("/todo")
def get_todo():
    todo_id = session["todo_id"]
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{todo_id}")

    if response.status_code == 200:
        todo = response.json()
    else:
        todo = {"error": "No more TODOs!"}

    return render_template("todo.html", todo=todo)

@app.route("/next")
def next_todo():
    session["todo_id"] += 1  # Move to the next TODO
    return redirect(url_for("get_todo"))

if __name__ == "__main__":
    app.run(debug=True)
