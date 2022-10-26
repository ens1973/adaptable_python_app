from flask import Blueprint
from flask import jsonify

home_bp = Blueprint('home', __name__)

@home_bp.get('/')
def home():
    return jsonify(message='Hey yo!'), 200