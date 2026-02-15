import pytest
from unittest.mock import Mock
from codepal.api import API

@pytest.fixture
def api():
    return API()

def test_api_setup(api):
    assert api is not None

def test_api_success_request(api, monkeypatch):
    mock_response = Mock(status_code=200)
    monkeypatch.setattr('requests.get', lambda x: mock_response)
    assert api.make_request('url') == 200

def test_api_failure_request(api, monkeypatch):
    mock_response = Mock(status_code=404)
    monkeypatch.setattr('requests.get', lambda x: mock_response)
    assert api.make_request('url') == 404

def test_api_invalid_url(api):
    with pytest.raises(Exception):
        api.make_request(None)
