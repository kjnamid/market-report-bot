@echo off

set GEMINI_API_KEY=AIzaSyDp-R5NzyLHim_loE0jSHAeZABLiPbB2fk
set KAKAO_REST_API_KEY=7ccf2a09e391f3449d92a4bd254e24ea
set KAKAO_REFRESH_TOKEN=Sw0DDay2P3PN7DvjGeYsgJ1a3moDO7EQAAAAAgoXACcAAAGeeSBlSqew61y3DOUZ

python main.py

pause


#################################################################
#client secret : GpVZs7qSQ8Gmcsf2WvfIImpmcgBMgO1b


#acces_token : 
#Ko11HWmtvfv1eGPrflw1_KyY8-ALZ5LbgRdj1EDJRZm9EbyB3v2PgwAAAAQKFxItAAABnnkY0PvGDcCf5rkkeA
#tmNjEHGAGgGraxHtZ-Dzyi3hrPrP7dcRAAAAAQoXACcAAAGeeSBlUKew61y3DOUZ


#Refresh_token
#0-fDqTZhmqqFgXCNcpIk7lZMRB4MPnEnAAAAAgoXC9cAAAGeeP7flKew61y3DOUZ
#Sw0DDay2P3PN7DvjGeYsgJ1a3moDO7EQAAAAAgoXACcAAAGeeSBlSqew61y3DOUZ


#curl -X POST "https://kauth.kakao.com/oauth/token" -d "grant_type=authorization_code" -d "client_id=7ccf2a09e391f3449d92a4bd254e24ea" -d "client_secret=GpVZs7qSQ8Gmcsf2WvfIImpmcgBMgO1b" -d "redirect_uri=https://localhost" -d "code=Ko11HWmtvfv1eGPrflw1_KyY8-ALZ5LbgRdj1EDJRZm9EbyB3v2PgwAAAAQKFxItAAABnnkY0PvGDcCf5rkkeA"

#* 정상적으로 설정되었는지 확인하는 방법 "
#curl -X GET "https://kapi.kakao.com/v2/user/me" -H "Authorization: Bearer tmNjEHGAGgGraxHtZ-Dzyi3hrPrP7dcRAAAAAQoXACcAAAGeeSBlUKew61y3DOUZ"