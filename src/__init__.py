from flask import Flask

def create_app(test_config=None):

    app = Flask(__name__)

    from .home import home_bp
    app.register_blueprint(home_bp, url_prefix='/')

    return app