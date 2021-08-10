import json
from datetime import datetime

from flask import make_response, request, jsonify
from flask.blueprints import Blueprint
from unidecode import unidecode

from app.models import Purchase
from app.utils.db import db
from app.utils import purchase_status as STATUS


purchase_bp = Blueprint('purchase_bp', __name__, url_prefix='/purchases')

@purchase_bp.route('user/<user_id>', methods=['GET'])
def get_by_user(user_id):
    try:
        purchases = Purchase.query.filter_by(user_id=user_id).all()
        if purchases:
            return jsonify([i.serialize for i in purchases])
        return make_response({}), 200
    except Exception as e:
        return make_response({'error': e}), 400

@purchase_bp.route('/<purchase_id>', methods=['GET'])
def retrieve_by_id(purchase_id):
    try:
        purchase = Purchase.query.filter_by(purchase_id=purchase_id).first()
        if purchase:
            return purchase.as_dict()
        return make_response({}), 200
    except Exception as e:
        return make_response({'error': e}), 400

@purchase_bp.route('', methods=['POST'])
def create():
    try:
        data = json.loads(request.data)
        
        purchase = Purchase(
            user_id=data['user_id'],
            product_id=data['product_id'],
            size=data['size'],
            color=data['color'],
        )
        db.session.add(purchase)
        db.session.commit()
        db.session.flush()
        return make_response(purchase.serialize), 200
    except Exception as e:
        return make_response({'error': e}), 400

@purchase_bp.route('/<purchase_id>', methods=['PATCH'])
def update(purchase_id):
    try:
        data = json.loads(request.data)
        purchase = Purchase.query.filter_by(purchase_id=purchase_id).first()
        purchase.updated_at = datetime.now()

        if 'status' in data:
            if data['status'] == STATUS.CANCELED:
                purchase.canceled_at = datetime.now()
                purchase.reason = unidecode(data['reason']) if 'reason' in data else None
            purchase.status = data['status']

        db.session.commit()
        return make_response(purchase.serialize), 200
    except Exception as e:
        return make_response({'error': e}), 400
