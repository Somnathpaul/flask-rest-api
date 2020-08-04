from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# app
app = Flask(__name__)

# route 
@app.route('/', methods=['GET'])
def home():
    return jsonify( {'name:':'flask' } )

# server
if __name__ == "__main__":
    app.run(debug=True)