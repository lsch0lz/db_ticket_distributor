import os

from flask import Flask
from . import db
from . import auth
from . import search

from . import blog

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

    db.init_app(app)

    app.register_blueprint(auth.bp)

    app.register_blueprint(blog.bp)
    app.add_url_rule("/", endpoint="index")

    app.register_blueprint(search.bp)

    return app
