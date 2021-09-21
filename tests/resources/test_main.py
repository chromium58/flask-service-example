import json
import multiprocessing

multiprocessing.set_start_method("fork")  # Fix for https://github.com/pytest-dev/pytest-flask/issues/104

pytest_plugins = [
    "tests.fixture.fixtures",
]


def test_get_weather(http_client):
    response = http_client.post(
        '/api/test',
        json={
            "city": "RandomCity"
        }
    )
    assert response.status_code == 200
    resp_data = json.loads(response.data)
    assert isinstance(resp_data, dict)
