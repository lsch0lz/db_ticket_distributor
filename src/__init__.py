import os

from flask import Flask
from . import db
from . import auth

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="DEV",
        DATABASE=os.path.join(app.instance_path, "user.sqlite")
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def hello():
        return str(os.path.join(app.instance_path, "user.sqlite"))

    db.init_app(app)

    app.register_blueprint(auth.bp)

    return app
