import os
from dotenv import load_dotenv

load_dotenv()

from market import get_market_data
from ai_summary import create_summary
from kakao import get_access_token, send_message


# print("GEMINI =", os.getenv("GEMINI_API_KEY"))
# print("KAKAO =", os.getenv("KAKAO_REST_API_KEY"))
# print("REFRESH =", os.getenv("KAKAO_REFRESH_TOKEN"))
# print("KaKao Access Token =",  get_access_token())

# send_message("카카오 API test 성공!!!!!!!!!!!!")


def main():

    market_data = get_market_data()

    summary = create_summary(market_data)

    print(summary)

    send_message(summary)

if __name__ == "__main__":
    main()