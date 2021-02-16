from flask import Blueprint
from flask_restful import Api

# local imports
from app.resources.main import Example

api_bp = Blueprint('api', __name__, template_folder="templates")
api = Api(api_bp)

# Route
api.add_resource(Example, '/test')
