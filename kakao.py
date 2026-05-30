import os
import json
import requests

SEND_URL = (
    "https://kapi.kakao.com"
    "/v2/api/talk/memo/default/send"
)

TOKEN_URL = (
    "https://kauth.kakao.com/oauth/token"
)

def send_message(text):

    access_token = os.getenv(
        "KAKAO_ACCESS_TOKEN"
    )

    headers = {
        "Authorization":
        f"Bearer {access_token}"
    }

    template = {
        "object_type": "text",
        "text": text,
        "link": {
            "web_url":
            "https://finance.naver.com"
        }
    }

    requests.post(
        SEND_URL,
        headers=headers,
        data={
            "template_object":
            json.dumps(template)
        }
    )