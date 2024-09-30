import os
import requests


address = "localhost"

port = "8000"

def make_request(address: "str", port: "int", params: "dict[str, str]", ):
    return True

def test_status() -> None:
    url = f"http://{address}:{port}/status"
    r = request.get(url = url)
    assert (r) == 1

