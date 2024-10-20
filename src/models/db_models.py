from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# User model class
class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Contact model class
class Contact(db.Model):
    __tablename__ = 'Contacts'
    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(200), nullable=False)
    LastName = db.Column(db.String(200), nullable=False)
    PhoneNo = db.Column(db.String(10), nullable=False)
    Email = db.Column(db.String(50), nullable=False)
    Area = db.Column(db.String(50), nullable=False)
    City = db.Column(db.String(30), nullable=False)
    State = db.Column(db.String(30), nullable=False)
    Pincode = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(80), nullable=False)
