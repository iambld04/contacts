from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import SQLAlchemyError
from src.models.db_models import Contact, db
from src.constants.messages import messages
from src.services.contact_service import create_new_contact,get_a_contact,get_all_contacts,update_a_contact,delete_a_contact

@jwt_required()
def create_contact():
    try:
        if not request.is_json:
            return jsonify({'message': messages["REQUEST_JSON"]}), 400
        
        data = request.get_json()
        if not data:
            return jsonify({'message': messages["DATA_REQUIRED"]}), 400

        current_user = get_jwt_identity()
        create_new_contact(data,current_user)
        return jsonify({'message': messages["CONTACT_CREATED"]}), 201

    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"message": messages["DATABASE_ERROR"]}), 500

    except Exception:
        return jsonify({"message": messages["ERROR_OCCURRED"]}), 500


@jwt_required()
def get_contact(id):
    try:
        
        current_user = get_jwt_identity()
        contact = Contact.query.get_or_404(id)
        if contact.username != current_user:
            return jsonify({'message': messages["ACCESS_DENIED"]}), 403
        contact_data = get_a_contact(contact)
        return jsonify(contact_data)

    except SQLAlchemyError:
        return jsonify({"message": messages["DATABASE_ERROR"]}), 500

    except Exception:
        return jsonify({"message": messages["ERROR_OCCURRED"]}), 500


@jwt_required()
def get_contacts():
    
    try:
        current_user = get_jwt_identity()
        contacts = Contact.query.filter_by(username=current_user).all()
    
        output = get_all_contacts(contacts)
        
        if not output:
            return jsonify({'message': messages["NO_ENTRIES"]}), 404
        return jsonify({'Contacts': output})

    except SQLAlchemyError:
        return jsonify({"message": messages["DATABASE_ERROR"]}), 500

    except Exception:
        return jsonify({"message": messages["ERROR_OCCURRED"]}), 500

@jwt_required()
def update_contact(id):
    try:
        if not request.is_json:
            return jsonify({'message': messages["REQUEST_JSON"]}), 400
        
        data = request.get_json()
        
        if not data:
            return jsonify({'message': messages["DATA_REQUIRED"]}), 400

        current_user = get_jwt_identity()
        contact = Contact.query.get_or_404(id)
        
        if contact.username != current_user:
            return jsonify({'message': messages["ACCESS_DENIED"]}), 403

        update_a_contact(data,contact)
        
        return jsonify({'message': messages["CONTACT_UPDATED"]})

    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"message": messages["DATABASE_ERROR"]}), 500

    except Exception:
        return jsonify({"message": messages["ERROR_OCCURRED"]}), 500


@jwt_required()
def delete_contact(id):
    try:
        current_user = get_jwt_identity()
        contact = Contact.query.get_or_404(id)
        
        if contact.username != current_user:
            return jsonify({'message': messages["ACCESS_DENIED"]}), 403

        delete_a_contact(contact)
        
        return jsonify({'message': messages["CONTACT_DELETED"]})

    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"message": messages["DATABASE_ERROR"]}), 500

    except Exception:
        return jsonify({"message": messages["ERROR_OCCURRED"]}), 500

def missing_id():
    return jsonify({"message": messages["REQUIRE_ID"]}), 400