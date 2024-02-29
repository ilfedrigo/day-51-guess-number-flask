from flask import Flask

app = Flask(__name__)

def big_center(function):
    def wrapper():
        return f"<h1 style='text-align:center'>{function()}</h1>"
    return wrapper

def make_bold(function):
    def wrapper():
        return f"<b>{function()}<b>"
    return wrapper

def underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

def make_italic(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

@app.route('/')
def hello_world():
    return "Hello world!"

@app.route("/bye")
@big_center
@make_bold
@make_italic
@underline

def bye():
    return "Bye!"

@app.route("/<name>")
def greet(name):
    return f"Hello there {name}"

if __name__ == "__main__":
    app.run(debug=True)