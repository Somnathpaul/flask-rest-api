from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from markupsafe import escape

import os

# app
app = Flask(__name__)

# route 
@app.route('/', methods=['GET'])
def home():
    return jsonify( {'name:':'flask' } )

@app.route('/about', methods=['GET'])
def about():
    return 'Web application REST API made with flask!'

@app.route('/user/<username>')
def user(username):
    return 'User %s' % escape(username)

# server
if __name__ == "__main__":
    app.run(debug=True)