from enum import unique
from app import app 
from flask_sqlalchemy import SQLAlchemy

app.config["SECRET_KEY"] = ""
app.config["SQLALCHEMY_DATABASE_URI"] = ""
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

class User(db.model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(70), unique=True)
    password = db.Column(db.string(50), nullable= False)

