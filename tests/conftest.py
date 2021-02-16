import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app('testing')
    api_client = app.test_client()

    yield api_client
