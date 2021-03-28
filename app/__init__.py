import logging
from flask import Flask, got_request_exception

# local import
from instance.config import app_config
from .routes import api_bp


def log_exception(sender, exception, **extra):
    """ Log an exception to our logging framework """
    sender.logger.error(
        f'Got exception during processing. Error message: {exception}'
    )


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    route_path = app.config.get('ROUTE_PATH')
    app.config['static_url_path'] = f'{route_path}/swagger_static/'
    app.config['static_folder'] = 'app/swagger_static/static'
    app.config['SWAGGER'] = {
        'title': 'API Swagger',
        'doc_dir': './app/swagger_docs/',
        'version': '3.2.2',
        'uiversion': 3,
        'specs_route': f'{route_path}/swagger',
        'description': "Api Documentation",
        'static_url_path': f'{route_path}/static',
        "specs": [
            {
                "endpoint": 'docs',
                "route": f'{route_path}/pipeline.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "termsOfService": ""
    }

    log_level = logging.getLevelName(
        app.config.get("FLASK_LOG_LEVEL", "DEBUG")
    )

    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=log_level
    )

    app.logger.addHandler(logging.StreamHandler())
    got_request_exception.connect(log_exception, app)
    app.register_blueprint(api_bp, url_prefix=route_path)

    return app
