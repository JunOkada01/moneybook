from flask import jsonify, request
from . import main

@main.route('/')
def hello():
    return "Hello from Flask!"
