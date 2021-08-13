import os
import json
from datetime import datetime, date
from random import randint
from time import time
from uuid import uuid4

from flask import make_response, request, jsonify
from flask.blueprints import Blueprint
import pytz
from sqlalchemy import desc
from unidecode import unidecode

from app.models import Purchase
from app.utils.db import db
from app.utils import purchase_status as STATUS


purchase_bp = Blueprint('purchase_bp', __name__, url_prefix='/purchases')

@purchase_bp.route('user/<user_id>', methods=['GET'])
def get_by_user(user_id):
    try:
        purchases = Purchase.query.filter_by(user_id=user_id).order_by(desc(Purchase.created_at)).all()
        return jsonify([i.serialize for i in purchases])
    except Exception as e:
        return make_response({'error': str(e)}), 400

@purchase_bp.route('/<purchase_id>', methods=['GET'])
def retrieve_by_id(purchase_id):
    try:
        purchase = Purchase.query.filter_by(purchase_id=purchase_id).first()
        if purchase:
            return purchase.as_dict()
        return make_response({}), 200
    except Exception as e:
        return make_response({'error': str(e)}), 400

@purchase_bp.route('', methods=['POST'])
def create():
    try:
        data = json.loads(request.data)
        
        purchase = Purchase(
            user_id=data['user_id'],
            product_id=data['product_id'],
            size=data['size'],
            color=data['color'],
            payment_type=data['payment_type'],
            address=data['address'],
        )
        purchase.purchase_id = uuid4().hex
        purchase.purchase_code = str(randint(1000,9999)) + str(time()).split('.')[0]
        db.session.add(purchase)
        db.session.commit()
        db.session.flush()
        return make_response(purchase.serialize), 200
    except Exception as e:
        return make_response({'error': str(e)}), 400

@purchase_bp.route('/<purchase_id>', methods=['PATCH'])
def update(purchase_id):
    try:
        data = json.loads(request.data)
        purchase = Purchase.query.filter_by(purchase_id=purchase_id).first()
        if not purchase:
            return make_response({'error': 'result not found'}), 400

        purchase.updated_at = datetime.utcnow()

        if 'status' in data:
            if data['status'] == STATUS.CANCELED:
                now = datetime.now()
                result = now - purchase.created_at.replace(tzinfo=None)

                if result.days >= int(os.getenv('EXPIRES_IN')):
                    return make_response({'error': f'you cannot cancel purchase because has passed {os.getenv("EXPIRES_IN")} days'}), 406
                purchase.canceled_at = now
                purchase.reason = unidecode(data['reason']) if 'reason' in data else None
            purchase.status = data['status']
        
        if 'address' in data:
            for k,v in data['address'].items():
                if type(data['address'][k]) == str:
                    data['address'][k] = unidecode(data['address'][k])
            purchase.address = data['address']

        db.session.commit()
        return make_response(purchase.serialize), 200
    except Exception as e:
        return make_response({'error': str(e)}), 400
