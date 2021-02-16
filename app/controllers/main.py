from flask import current_app
import requests


class ExampleClass(object):
    def __init__(self):
        self.weather_site = current_app.config.get('WEATHER_SITE')

    def get_city_weather(self, city: str) -> dict:
        weather = requests.get(f'{self.weather_site}/{city}?format=3')
        current_app.logger.info(weather.text)
        return {"result": f"Today in {weather.text}"}
