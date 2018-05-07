from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/hello")
def hello():
    return "<p>Hello, there!</p>"


@app.route("/about")
def about():
    return "<h1>About Us<h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
