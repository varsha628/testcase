from requests import Response
import json
from typing import Any,List,Dict


def mock_api_success(*args:List[Any],**kwargs:Dict[str,Any]) ->Response:
    """Mock for response success"""
    result={
        "ok": "true",
        "channels": [
        {
            "id": "C086YFZ9DDL",
            "name": "all-shilpa",
            "is_channel": "true",
            "is_group": "false",
            "is_im": "false",
            "updated": 1735880230018,
            "shared_team_ids": [
                "T0877KXMYAY"
            ],
            "properties": {
                "canvas": {
                    "file_id": "F086YFZAKSA",
                    "is_empty": "false",
                    "quip_thread_id": "DOF9AA4MjtB"
                },
                "use_case": "welcome"
            },
            "previous_names": [
                "all-slack"
            ],
            "num_members": 4
        },
        ]
    }

    url="https://slack.com/api/conversations.list"
    response=Response()
    response.url=url
    response.status_code=200
    response._content=bytes(json.dumps(result),encoding="utf-8")
    return response