from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world! From CS50!"


# app.run()