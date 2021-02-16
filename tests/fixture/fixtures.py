import pytest
from tests.fake_servers import fake_http_server
from app import create_app


@pytest.fixture
def http_client():
    app = create_app('testing')
    host, port = fake_http_server.get_free_tcp_port()
    app.config["WEATHER_SITE"] = 'http://{0}:{1}'.format(host, port)
    with fake_http_server.app.run(host, port):
        yield app.test_client()


@pytest.fixture
def broken_http_client():
    app = create_app('testing')
    app.config["WEATHER_SITE"] = 'http://127.0.0.1:1'
    yield app.test_client()
