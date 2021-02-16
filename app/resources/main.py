from flask import current_app, request
from flask_restful import Resource
from flasgger import swag_from
from app.helpers.exceptions import CriticalError
from ..controllers.main import ExampleClass
from .common import handle_errors


class Example(Resource):
    @swag_from('../swagger_docs/main.yml', methods=['POST'])
    def post(self):
        json_data = request.json
        current_app.logger.info(
            'Input parameters are: {}'.format(json_data)
        )
        city = json_data.get('city', '')

        try:
            example = ExampleClass()
            result = example.get_city_weather(city)
        except CriticalError as err:
            return handle_errors(err.message)
        return result
