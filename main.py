from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world!"

@app.route("/bye")
def bye():
    return "bye!"

@app.route("/<name>")
def greet(name):
    return f"Hello there {name}"

if __name__ == "__main__":
    app.run(debug=True)