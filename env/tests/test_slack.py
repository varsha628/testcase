from src.slack import SlackAPI, a
from unittest.mock import patch
import requests
from tests.mocks.functions import  mock_api_success
from typing import Any
import pytest


def test_invalid_token():
    """Test for invalid Slack API token"""
    slack_api = SlackAPI("invalid-token")
    response = slack_api.get_conversations_list("url")
    assert response is None, "Expected None for invalid token."

def test_network_error():
    """Test for network error during API call"""
    with patch("requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError
        slack_api = SlackAPI("valid-slack-token")
        response = slack_api.get_conversations_list("url")
        assert response is None, "Expected None for a network error."


def test_empty_token():
    """Test for empty Slack API token."""
    slack_api = SlackAPI("")
    response = slack_api.get_conversations_list("url")
    assert response is None, "Expected None for empty token."

def  test_mocks(mocker:Any)->None:
    """testcase for get method using mocks.
     Args:
     mocker (Any): A mocker
    """
    mocker.patch("requests.get",mock_api_success)
    response=a.get_conversations_list(url="test_url")
    data=response.json()
    assert response.status_code == 200

@pytest.mark.vcr()
def test_vcr()->None:
     """testcase for get method using vcr"""
     response=a.get_conversations_list(url="https://slack.com/api/conversations.list") 
     assert response.status_code == 200



