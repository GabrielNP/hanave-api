from flask import make_response, request, jsonify
from flask.blueprints import Blueprint

from app.models import Product


product_bp = Blueprint('product_bp', __name__, url_prefix='/products')

@product_bp.route('/', methods=['GET'])
def get_all():
    try:
        category = request.args.get('category')
        products = Product.query.filter(Product.price != None)
        if category:
            products = products.filter_by(category=category)
        return jsonify([i.serialize for i in products])
    except Exception as e:
        return make_response({'error': e}), 400

@product_bp.route('/<product_id>', methods=['GET'])
def retrieve_by_id(product_id):
    try:
        products = Product.query.filter_by(id=product_id).first()
        if products:
            return products.as_dict()
        return make_response({}), 200
    except Exception as e:
        return make_response({'error': e}), 400
