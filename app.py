from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    commit_id = os.getenv("COMMIT_SHA", "unknown")
    return render_template("index.html", commit_id=commit_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)