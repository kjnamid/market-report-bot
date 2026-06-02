import ast
from datetime import datetime, timedelta

import requests


NAVER_INDEX_URL = "https://api.finance.naver.com/siseJson.naver"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0 Safari/537.36"
    )
}


def _get_naver_index_close(code):
    today = datetime.now()
    start_date = (today - timedelta(days=14)).strftime("%Y%m%d")
    end_date = today.strftime("%Y%m%d")

    response = requests.get(
        NAVER_INDEX_URL,
        params={
            "symbol": code,
            "requestType": "1",
            "startTime": start_date,
            "endTime": end_date,
            "timeframe": "day",
        },
        headers=HEADERS,
        timeout=10,
    )
    response.raise_for_status()

    rows = ast.literal_eval(response.text.strip())
    data_rows = [row for row in rows[1:] if len(row) >= 5]
    if not data_rows:
        raise ValueError(f"네이버 금융 지수 데이터를 찾을 수 없습니다: {code}")

    close_price = data_rows[-1][4]
    return f"{close_price:,.2f}"


def get_market_data():
    result = []

    try:
        kospi_close = _get_naver_index_close("KOSPI")
        kosdaq_close = _get_naver_index_close("KOSDAQ")

        result.append(f"KOSPI 종가: {kospi_close}")
        result.append(f"KOSDAQ 종가: {kosdaq_close}")

        # print(f"KOSPI 종가: {kospi_close}")
        # print(f"KOSDAQ 종가: {kosdaq_close}")

    except Exception as e:
        result.append(f"지수 조회 실패: {e}")
        print(f"지수 조회 실패: {e}")

    return "\n".join(result)
