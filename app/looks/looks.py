from flask import make_response, request, jsonify
from flask.blueprints import Blueprint

from app.models import Look

look_bp = Blueprint('look_bp', __name__, url_prefix='/looks')

@look_bp.route('/', methods=['GET'])
def get_all():
    try:
        looks = Look.query.all()
        return jsonify([i.serialize for i in looks])
    except Exception as e:
        return make_response({'error': str(e)}), 400

@look_bp.route('/<look_id>', methods=['GET'])
def retrieve_by_id(look_id):
    try:
        looks = Look.query.filter_by(id=look_id).first()
        if looks:
            return looks.as_dict()
        return make_response({}), 200
    except Exception as e:
        return make_response({'error': str(e)}), 400
