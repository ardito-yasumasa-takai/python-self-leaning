from app import resources

from flask import Blueprint, Flask

from flask_restplus import Api


def create_app(**kargs):
    flask_app = Flask(__name__)
    blueprint = Blueprint("api", __name__)
    api = Api(
        app=blueprint,
        doc="/",
        description="FlaskSelfTraining",
        title="FlaskSelfTraining API",
        authorizations={
            'Bearer Auth': {
                'type': 'apiKey',
                'in': 'header',
                'name': 'Authorization',
            },
        },
        security='Bearer Auth'
    )

    flask_app.register_blueprint(blueprint, url_prefix="/api")
    resources.setup_namespaces(api)

    return flask_app
