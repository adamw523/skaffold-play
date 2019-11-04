import sys, time
from flask import Flask, render_template

print("I'm starting")

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Worlds!"

@app.route("/test")
def test():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

    