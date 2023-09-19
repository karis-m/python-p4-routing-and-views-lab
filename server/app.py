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
    print('hello')
    return f'hello'

@app.route('/count/<int:parameter>')
def count(parameter):
    return '\n'.join(map(str, range(parameter))) + '\n'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        print('Invalid Operation')
    
    return str(result)
