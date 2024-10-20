from flask import Flask,request
from flask_jwt_extended import JWTManager
from datetime import timedelta
from dotenv import load_dotenv
import os
from src.constants import db_config as constant
from src.models.db_models import db
from src.controllers.auth_controller import register_user, login_user 
from src.controllers.contact_controller import create_contact, get_contact, get_contacts, update_contact, delete_contact,missing_id 
load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"mssql+pyodbc://{constant.username}:{os.getenv('DATABASE_PASSWORD')}@{constant.server_name}/{constant.database_name}?driver={constant.driver}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

expire_time = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=expire_time)

jwt = JWTManager(app)
db.init_app(app)

# 1. Register Route
@app.route('/register', methods=['POST'])
def register():
    return register_user()

# 2. Login Route
@app.route('/login', methods=['POST'])
def login():
    return login_user()

# 3. Create a New Contact and get all contacts route
@app.route('/contacts', methods=['GET','POST'])
def handle_contacts():
    if request.method == 'GET':
        return get_contacts()
    elif request.method == 'POST':
        return create_contact()
    
@app.route('/contacts/', methods=['GET','PUT','DELETE'])
def missing_contact_id():
    return missing_id()

# 4. Get a Specific Contact and update a contact and delete a contact by ID
@app.route('/contacts/<int:id>', methods=['GET','PUT','DELETE'])
def handle_contacts_by_id(id):
    if request.method == 'GET':
        return get_contact(id)
    elif request.method == 'PUT':
        return update_contact(id)
    elif request.method == 'DELETE':
        return delete_contact(id)

if __name__ == '__main__':
    port_number = int(os.getenv('FLASK_PORT_NUMBER'))
    app.run(debug=True,host='127.0.0.2',port=port_number)
    
