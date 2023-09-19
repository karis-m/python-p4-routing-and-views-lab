#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'
if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/print/<string:parameter>')
def print_parameter(parameter):
    return f'<h1>The captured parameter is: {parameter}</h1>'

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = list(range(parameter))
    return f'<h1>{numbers}</h1>'