# src/auth_routes/auth.py

from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import SQLAlchemyError
from src.models.db_models import Users, db 
from src.constants.messages import messages 

# Function to handle user registration
def register_user():
    try:
        if not request.is_json:
            return jsonify({'message': messages["REQUEST_JSON"]}), 400
        
        data = request.get_json()
        if not data or not data.get("username") or not data.get("password"):
            return jsonify({"message": messages["REQUIRED"]}),400
        
        hashed_password = generate_password_hash(data['password'], method='scrypt')

        new_user = Users(username=data['username'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': messages["USER_CREATED"]}), 201
    
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"Error": messages["DATABASE_ERROR"],"Details":str(e)}),500
    
    except Exception as e:
        return jsonify({"message": messages["ERROR_OCCURRED"],"Details":str(e)}),500

# Function to handle user login
def login_user():
    try:
        if not request.is_json:
            return jsonify({'message': messages["REQUEST_JSON"]}), 400
        
        data = request.get_json()
        if not data or not data.get("username") or not data.get("password"):
            return jsonify({"message":messages["REQUIRED"]}),400
        
        user = Users.query.filter_by(username=data['username']).first()

        if not user or not check_password_hash(user.password, data['password']):
            return jsonify({'message': messages["INVALID_USERNAME_OR_PASSWORD"]}), 401

        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token)
    
    except SQLAlchemyError as e:
        return jsonify({"Error": messages["DATABASE_ERROR"],"Details":str(e)}),500
    
    except Exception as e:
        return jsonify({"message":messages["ERROR_OCCURRED"],"Details":str(e)}),500


