from flask import Flask
from .utils import get_static_folder

def create_app(test_config=None):

    app = Flask(__name__)

    static_folder=get_static_folder()

    app.config.from_mapping(
        static_folder=static_folder,
    )

    from .home import home_bp
    app.register_blueprint(home_bp, url_prefix='/')

    return app