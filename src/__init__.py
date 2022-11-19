from flask import Flask

# from datetime import datetime
# from datetime import timedelta
# from datetime import timezone
# from flask_jwt_extended import current_user
# from flask_jwt_extended import create_access_token
# from flask_jwt_extended import set_access_cookies
# from flask_jwt_extended import get_jwt

from flask_cors import CORS

# from os import path as os_path
from dotenv import load_dotenv
from os import getenv



def create_app(script_info=None):

    load_dotenv()

    app = Flask(__name__)
    current_env = getenv('ENV')
    if (current_env == 'development'):
        app.config.from_object("src.config.DevelopmentConfig")
    else:
        app.config.from_object("src.config.ProductionConfig")

    # app.logger.info(f"Config: {config_name}")

    # #  Logging
    # import logging

    # logging.basicConfig(
    #     level=app.config["LOG_LEVEL"],
    #     format="%(asctime)s %(levelname)s: %(message)s " "[in %(pathname)s:%(lineno)d]",
    #     datefmt="%Y%m%d-%H:%M%p",
    # )


    # @app.after_request
    # def refresh_expiring_jwts(response):
    #     # response.headers['Access-Control-Allow-Origin'] = '*'
    #     # response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    #     # response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
        
    #     try:
    #         exp_timestamp = get_jwt()["exp"]
    #         now = datetime.now(timezone.utc)
    #         target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
    #         if target_timestamp > exp_timestamp:
    #             access_token = create_access_token(identity=current_user)
    #             set_access_cookies(response, access_token)
    #     except (RuntimeError, KeyError):
    #         # Case where there is not a valid JWT. Just return the original respone
    #         return response
    #     return response

    # static_frontend = os_path.join('..', 'static_frontend');
    register_extensions(app)
        
    from .api import api_bp
    app.register_blueprint(api_bp, url_prefix="/v1/api")

    # from .health.check import check_bp
    # app.register_blueprint(check_bp, url_prefix="/check")

    @app.route("/")
    def hello_world():
        return "<p>hi there!</p>"

    CORS(app)

    return app

def register_extensions(app):
    # pass
    from .extensions import jwt
    jwt.init_app(app)
    from .extensions import db_init
    db_init(app.config.get('ENV'))
    from .extensions import CustomEncoder
    app.json_encoder = CustomEncoder
    # from .extensions import db
    # db.init_app(app)
    # from .extensions import ma
    # ma.init_app(app)