import logging
import os

from dotenv import load_dotenv
from flask import Flask
from flask.helpers import make_response

from app.api.api import api_bp
from app.carts.carts import cart_bp
from app.products.products import product_bp
from app.purchases.purchases import purchase_bp
from app.users.users import user_bp
from app.utils.db import db
from app.looks.looks import look_bp

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.logger.setLevel(logging.INFO)
db.init_app(app)

app.register_blueprint(cart_bp)
app.register_blueprint(product_bp)
app.register_blueprint(purchase_bp)
app.register_blueprint(user_bp)
app.register_blueprint(api_bp)
app.register_blueprint(look_bp)

@app.errorhandler(400)
def bad_request(error):
    return make_response({"detail": "Bad Request", "error_code": 400}), 400

@app.errorhandler(404)
def not_found(error):
    return make_response({"detail": "Not Found", "error_code": 404}), 404

@app.errorhandler(405)
def server_error(error):
    return make_response({"detail": "Method Not Allowed", "error_code": 405}), 405

@app.errorhandler(500)
def server_error(error):
    return make_response({"detail": "Server Error", "error_code": 500}), 500

