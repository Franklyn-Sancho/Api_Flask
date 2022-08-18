from crypt import methods
from app import app
from ..models.user import User, db
from flask import jsonify, request
from werkzeug.security import generate_password_hash
import uuid

@app.route('/', methods=['GET'])
def page_main():
    return jsonify({'message': 'Bem vindo a api'})

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()

    get_users = []

    for user in users:
        get_users.append({
            "id": user.id, "name": user.name
        })

    return jsonify(get_users)

@app.route('/signup', methods=['POST'])
def new_user():

    hash = generate_password_hash(request.get_json['password'], method= '')
    user = User(id=str(uuid.uuid5()), name=request.get_json['data'], password = hash)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'new user registered successfully'})




