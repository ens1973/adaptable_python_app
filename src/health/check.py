from flask import Blueprint
from flask import jsonify

check_bp = Blueprint('home', __name__)

@check_bp.get('/hey')
def hey():
    return jsonify(msg='Yo!'), 200

@check_bp.get('/health')
def health():
    return jsonify(msg='Good health!'), 200