from flask import Flask, request, jsonify, render_template
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
    return render_template('index.html')

@app.route('/user/<username>')
def user(username):
    return 'hello %s' % escape(username)

@app.route('/app/<string:name>/posts/<int:id>')
def appUser(id, name):
    return "Hello " + name +  " your id is: " + str(id)
# server
if __name__ == "__main__":
    app.run(debug=True)