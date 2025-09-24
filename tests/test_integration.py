import requests

def test_server_running():
    r = requests.get("http://localhost:5000")
    assert r.status_code == 200
    assert "Hello World" in r.text
