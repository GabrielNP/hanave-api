from flask import jsonify, make_response
from flask.blueprints import Blueprint

from app.models import User


user_bp = Blueprint('user_bp', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
def get_all():
    try:
        users = User.query.all()
        return jsonify([i.serialize for i in users])
    except Exception as e:
        return make_response({'error': e}), 400

@user_bp.route('/<user_id>', methods=['GET'])
def retrieve_by_id(user_id):
    try:
        user = User.query.filter_by(id=user_id).first()
        if user:
            return user.as_dict()
        return make_response({}), 200
    except Exception as e:
        return make_response({'error': e}), 400
