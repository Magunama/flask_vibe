import pytest

import app


@pytest.fixture(scope="module")
def client():
    client = app.create_app()
    client.testing = True

    yield client.test_client()
