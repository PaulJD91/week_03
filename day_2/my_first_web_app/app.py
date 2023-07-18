from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

@app.route('/<name>')
def greet(name):
    return  f"<h1>Hello {name}</h1>"

@app.route('/how')
def how_are_you():
    return f"<h1>How are you today?</h1>"

@app.route('/iwant/<food>')
def i_want_food(food):
    return f"<h1>I want {food}"
