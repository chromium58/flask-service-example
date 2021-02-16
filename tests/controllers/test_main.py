#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock
from app.controllers.main import ExampleClass
from app import create_app


class MainControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.test_client = ExampleClass()

    @patch('requests.get')
    def test_test_method(self, request_get_mock):
        get_return_value = "test"
        request_get_mock.return_value = MagicMock(str=MagicMock(return_value=get_return_value))
        request_get_mock.return_value.status_code = 200
        result = self.test_client.get_city_weather(city="RandomCity")
        assert isinstance(result, dict)
