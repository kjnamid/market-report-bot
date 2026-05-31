import os
import json
import requests

TOKEN_URL = "https://kauth.kakao.com/oauth/token"

SEND_URL = (
    "https://kapi.kakao.com"
    "/v2/api/talk/memo/default/send"
)

def get_access_token():

    client_id = os.getenv("KAKAO_REST_API_KEY")
    refresh_token = os.getenv("KAKAO_REFRESH_TOKEN")

    missing = [
        name for name, value in [
            ("KAKAO_REST_API_KEY", client_id),
            ("KAKAO_REFRESH_TOKEN", refresh_token)
        ] if not value
    ]
    if missing:
        raise RuntimeError(
            f"Missing Kakao environment variables: {', '.join(missing)}"
        )

    data = {
        "grant_type": "refresh_token",
        "client_id": client_id,
        "refresh_token": refresh_token
    }

    client_secret = os.getenv("KAKAO_CLIENT_SECRET")
    if client_secret:
        data["client_secret"] = client_secret

    response = requests.post(TOKEN_URL, data=data)

    if response.status_code != 200:
        raise RuntimeError(
            f"Failed to refresh Kakao access token: {response.status_code} {response.text}"
        )

    result = response.json()
    return result["access_token"]


def send_message(text):

    access_token = get_access_token()

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

    response = requests.post(
        SEND_URL,
        headers=headers,
        data={
            "template_object":
            json.dumps(template)
        }
    )

    result = response.json()
    # print(response.status_code, result)

    if response.status_code != 200 or result.get("result_code") != 0:
        raise RuntimeError(f"Kakao send failed: {response.status_code} {result}")

    response.raise_for_status()

    # print("카카오톡 발송 Test 성공 !!!!")