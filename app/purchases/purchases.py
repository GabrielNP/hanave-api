import os
import json
from datetime import datetime, date
from random import randint
from time import time
from uuid import uuid4

from flask import make_response, request, jsonify
from flask.blueprints import Blueprint
from sqlalchemy import create_engine, desc
from sqlalchemy.sql.expression import text
from unidecode import unidecode

from app.models import Product, Purchase
from app.utils.db import Parser, db
from app.utils import purchase_status as STATUS

SQL_ENGINE = create_engine(os.getenv('DATABASE_URL'), client_encoding='utf8', implicit_returning=True)


purchase_bp = Blueprint('purchase_bp', __name__, url_prefix='/purchases')

@purchase_bp.route('user/<user_id>', methods=['GET'])
def get_by_user(user_id):
    try:
        purchases = Purchase.query.filter_by(user_id=user_id).order_by(desc(Purchase.created_at)).all()
        # TODO: return also relational product names 
        # return jsonify([i.serialize for i in purchases])

        obj = [
            {
                "address": {
                "city": "San Antonio",
                "geolocation": {
                    "lat": "50.3467",
                    "long": "-20.1310"
                },
                "number": 6454,
                "street": "Hunters Creek Dr",
                "zipcode": "98234-1734"
                },
                "canceled_at": None,
                "color": "vermelho",
                "created_at": "2021-08-13T22:50:22+01:00",
                "delivery_forecast": "2021-09-13T23:05:19.173205+01:00",
                "payment_type": "card",
                "product_id": 4,
                "purchase_code": 1628895022,
                "purchase_id": "7d9f78cb-4daa-40a2-b97b-f316d95968dd",
                "reason": None,
                "size": "B",
                "status": "paid",
                "updated_at": "2021-08-13T23:05:19.173205+01:00",
                "user_id": 7,
                "category": "Camiseta Masculina Manga Longa",
                "color_available": [
                    "black"
                ],
                "description": "Camiseta Masculina De Manga Longa",
                "id": 4,
                "image": "https://fakestoreapi.com/img/71YXzeOuslL._AC_UY879_.jpg",
                "price": 34.9,
                "size_available": [
                    "S",
                    "M",
                    "B"
                ],
                "title": "Camiseta Manga Longa"
            },
            {
                "address": {
                "city": "San Antonio",
                "geolocation": {
                    "lat": "50.3467",
                    "long": "-20.1310"
                },
                "number": 6454,
                "street": "Hunters Creek Dr",
                "zipcode": "98234-1734"
                },
                "canceled_at": None,
                "color": "red",
                "created_at": "2021-06-13T22:55:28+01:00",
                "delivery_forecast": None,
                "payment_type": "card",
                "product_id": 4,
                "purchase_code": 93741628895328,
                "purchase_id": "d679fa34-6b77-4fb0-9c87-576a6a7ae870",
                "reason": None,
                "size": "B",
                "status": "pending_payment",
                "updated_at": "2021-08-13T22:55:28.089544+01:00",
                "user_id": 7,
                "category": "Sobretudo Feminino",
                "color_available": [
                    "lilac"
                ],
                "description": "Sobretudo Para o Inverno Lilas",
                "id": 9,
                "image": "https://fakestoreapi.com/img/51Y5NI-I5jL._AC_UX679_.jpg",
                "price": 120.0,
                "size_available": [
                    "S",
                    "M",
                    "B"
                ],
                "title": "Sobretudo Inverno"
            }
        ]
       
        return jsonify(obj)
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
