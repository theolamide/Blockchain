from flask import Flask
app = Flask(__name__)


@app.route("/home")
def hello():
    return "<h1>hello world</h1>"


@app.route("/newpage")
def newpage():
    return "<h1>This is new</h1>"


if __name__ == "__main__":
    app.run(debug=True)
