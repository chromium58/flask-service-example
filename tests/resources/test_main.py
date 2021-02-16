import json

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
