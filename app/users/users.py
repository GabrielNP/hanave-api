import json

from flask import request, make_response
from flask.blueprints import Blueprint

from app.models import User
from app.utils.db import db


user_bp = Blueprint('user_bp', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
def get_by_document_number():
    try:
        document_number = request.args.get('document_number')
        phone = request.args.get('phone')
        
        user = User.query

        if document_number:
            user = user.filter_by(document_number=document_number)
        
        if phone:
            user = user.filter_by(phone=phone)
        
        user = user.first()
            
        if user:
            return user.as_dict()
        return make_response({}), 200
    except Exception as e:
        return make_response({'error': str(e)}), 400

@user_bp.route('/<user_id>', methods=['GET'])
def retrieve_by_id(user_id):
    try:
        user = User.query.filter_by(id=user_id).first()
        if user:
            return user.as_dict()
        return make_response({}), 200
    except Exception as e:
        return make_response({'error': str(e)}), 400

@user_bp.route('/<user_id>', methods=['PATCH'])
def update(user_id):
    try:
        data = json.loads(request.data)
        user = User.query.filter_by(id=user_id).first()

        if 'first_name' in data:
            user.first_name = data['first_name']

        if 'last_name' in data:
            user.last_name = data['last_name']
        
        if 'phone' in data:
            user.phone = data['phone']
        
        if 'address' in data:
            user.address = data['address']

        db.session.commit()
        return user.as_dict()
    except Exception as e:
        return make_response({'error': str(e)}), 400

@user_bp.route('/', methods=['POST'])
def create():
    try:
        data = json.loads(request.data)

        user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone=data['phone'],
            username=data['username'],
            password=data['password'],
            email=data['email'],
            document_number=data['document_number']
        )

        db.session.add(user)
        db.session.commit()
        db.session.flush()

        return make_response(user.serialize), 200
    except Exception as e:
        return make_response({'error': str(e)}), 400
