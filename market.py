from pykrx import stock
from datetime import datetime

def get_market_data():

    today = datetime.now().strftime("%Y%m%d")

    result = []

    try:
        kospi = stock.get_index_ohlcv(today, "1001")
        kosdaq = stock.get_index_ohlcv(today, "2001")

        result.append(
            f"KOSPI 종가: {kospi.iloc[-1]['종가']}"
        )

        result.append(
            f"KOSDAQ 종가: {kosdaq.iloc[-1]['종가']}"
        )

    except Exception as e:
        result.append(f"지수 조회 실패: {e}")

    return "\n".join(result)