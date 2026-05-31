import os
from google import genai

def create_summary(market_data):

    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    prompt = f"""
당신은 한국 증시 20년차 베테랑 애널리스트다.

다음 시장 데이터를 분석하여
카카오톡용 시장 브리핑을 작성하라.

인사말은 생략할것.

{market_data}

형식

📈 시장요약

🔥 강세섹터

📊 특징

🎯 내일체크포인트

20줄 이내
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text