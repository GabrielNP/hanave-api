from flask import make_response, request, jsonify
from flask.blueprints import Blueprint

from app.models import Cart

cart_bp = Blueprint('cart_bp', __name__, url_prefix='/carts')

@cart_bp.route('/<user_id>', methods=['GET'])
def retrieve_by_user(user_id):
    try:
        users = Cart.query.filter_by(user_id=user_id)
        return jsonify([i.serialize for i in users])
    except Exception as e:
        return make_response({'error': str(e)}), 400
