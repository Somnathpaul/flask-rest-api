from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from markupsafe import escape

import os

# app
app = Flask(__name__) 

# connecting to database
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///flaskposts.db'
# create our database
db = SQLAlchemy(app)
# model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(20), nullable=False, default='anonymous')

    def __repr__(self):
        return 'Blog Post ' + str(self.id)

# dummy data

allPost = [
    {
        'no': 1,
        'title': 'REST API with flask',
        'body': 'Flask is cool but not as fast as node js!'
    },
    {
        'no': 2,
        'title': 'REST API with FastAPI ',
        'body': 'FastAPI is cool and as fast as node js!'
    },
]

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

@app.route('/post')
def postDoc():
    return render_template('post.html', posts=allPost)

@app.route('/post/api')
def getPostApi():
    return jsonify(allPost)

# server
if __name__ == "__main__":
    app.run(debug=True)