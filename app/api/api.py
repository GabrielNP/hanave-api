from flask.blueprints import Blueprint
from flask.helpers import make_response


api_bp = Blueprint('api_bp', __name__, url_prefix='/apí')

api_bp.route('/', methods=['GET'])
def handler():
    return make_response({"detail": "api is alive!"}), 200