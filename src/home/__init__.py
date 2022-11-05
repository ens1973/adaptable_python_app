from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import send_from_directory
from src.utils import get_static_folder

home_bp = Blueprint('home', __name__)

@home_bp.get('/')
def home():
    return jsonify(msg='Hey yo!'), 200

@home_bp.get('/health-check')
def health_check():
    return jsonify(msg='Good health!'), 200

@home_bp.get('/dingdong')
def dingdong():
    # return jsonify(message='Hey yo!'), 200
    # static_dir=static_folder
    static_dir = get_static_folder()
    return send_from_directory(static_dir, '1app.apk')

@home_bp.get('/dingdong-root-link')
def dingdong_root_link():
    return redirect("https://pns-update.vnpost.vn/download/app-pro_vnpost-release.apk", code=302)

