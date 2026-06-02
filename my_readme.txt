# Windows PowerShell로 로컬에서 싫행 시

$env:GEMINI_API_KEY="your_gemini_key"
$env:KAKAO_REST_API_KEY="your_kakao_rest_api_key"
$env:KAKAO_REFRESH_TOKEN="your_kakao_refresh_token"
pip install -r requirements.txt
python main.py


# GitHub에서 실제 값을 추가해야 합니다:

GitHub 리포지토리 → Settings → Secrets and variables → Actions
New repository secret 클릭
GEMINI_API_KEY: 실제 API 키 입력
KAKAO_REST_API_KEY: 실제 REST API 키 입력
KAKAO_REFRESH_TOKEN: 실제 refresh token 입력

주의: 실제 API 키나 토큰은 README, bat 파일, Python 파일에 적지 말고
.env 또는 GitHub Actions Secrets에만 저장합니다.

## 자동 실행 / 수동 실행
1. schedule
cron: '30 11 * * 1-5'
30 = 분 (30분)
11 = 시간 (11시)
* = 날짜 (매일)
* = 월 (매월)
1-5 = 요일 (월~금, 1=월요일, 5=금요일)
결과: 평일 매일 오전 11시 30분에 자동 실행
***  Git hub의 시간은 UTC임으로 한국 시간 표시는 = UTC 시간 + 9시간 

2. workflow_dispatch — 수동으로 실행 가능
GitHub 웹에서 Actions 탭 → "Run workflow" 버튼으로 언제든 실행

