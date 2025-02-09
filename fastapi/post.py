from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("get_post", post_id=1))  # Redirect to first post

@app.route("/posts/<int:post_id>")
def get_post(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")

    if response.status_code == 200:
        post = response.json()
    else:
        post_id = 0
        # post = response.json()
        post = {"error": "No more posts!"}

    return render_template("post.html", post=post, next_post_id=post_id + 1)

if __name__ == "__main__":
    app.run(debug=True)
