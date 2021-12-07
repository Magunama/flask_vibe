def test_landing(client):
    resp = client.get("/")
    assert "swagger-ui" in resp.data.decode("utf-8")
    assert resp.status_code == 200


def test_hello(client):
    resp = client.get("/hello/")
    assert "hello" in resp.data.decode("utf-8")
    assert resp.status_code == 200


def test_not_found(client):
    resp = client.get("/topkek")
    assert "error" in resp.data.decode("utf-8")
    assert resp.status_code == 404
