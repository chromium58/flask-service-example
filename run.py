#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from app import create_app
from flasgger import Swagger

config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name)

swagger = Swagger(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
