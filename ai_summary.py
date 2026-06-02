import os
import time
from google import genai
from google.genai import types
from google.genai import errors


MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
MAX_RETRIES = 3


def _fallback_summary(market_data, error):
    return f"""📈 시장요약

AI 요약 생성 실패: Gemini API가 일시적으로 응답하지 않습니다.
잠시 후 다시 실행해 주세요.

원본 시장 데이터
{market_data}

오류: {error}"""

def create_summary(market_data):

    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    prompt = f"""
당신은 한국 증시 분석 20년차 베테랑 애널리스트다.

인사말은 생략하고
다음 시장 데이터로 오늘 증시를 분석하여 카카오톡용 시장 브리핑을 작성하라.

{market_data}

형식

📈 시장요약

🔥 강세섹터(5개)

📊 특징주(대형주중에서 강한 매수세 유입이나 주목할 만한 상승이 이루어진 종목 5개)

🎯 현재 주요 테마와 관심 종목

20줄 이내
"""

    last_error = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config=types.GenerateContentConfig(
                    # 핵심 1: 창의성을 0으로 제한하여 매번 동일한 분석 결과 유도
                    temperature=0.0
                )
            )
            return response.text
        except errors.ServerError as e:
            last_error = e
            if attempt == MAX_RETRIES:
                break
            wait_seconds = 2 ** attempt
            print(
                f"Gemini API 일시 오류({e}). "
                f"{wait_seconds}초 후 재시도합니다. ({attempt}/{MAX_RETRIES})"
            )
            time.sleep(wait_seconds)

    return _fallback_summary(market_data, last_error)
