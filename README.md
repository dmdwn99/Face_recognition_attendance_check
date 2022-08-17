##2022-08-09
1. deepface 모델 성능 확인
2. 프로젝트 전체 구조 수정: APP, DB, DL_MODEL 등의 폴더 구조를 face_recognition, attendance_check로 재구성
3. DB를 Mysql로 하여 user_check table의 check 값 변경, 학번과 현재 날짜를 기준으로 하였음
4. deepface를 실행하면 deepface에서 인식한 사람을 attendance_check 모듈에서 DB 변경
5. 모델 작동은 되는데 사람 인식이 되지 않음

## 2022-08-14
1. fr_webpage 내 경로 __init__.py 파일 추가하여 패키지화
2. Deepface 모델에서 얼굴 인식하여 db 값 변경하였을 때 웹사이트에서 db 변경 확인
3. 얼굴 밝기의 따라 바운딩 박스 생성 확률의 차이가 있음, database img를 변경하니 얼굴 인식 됨
4. 모델 개선 및 웹페이지 기능 추가 및 개선 필요

## 2022-08-17
1. mysql table 중에서 user_check의 date_check column의 자료형을 str로 설정해줘야 함
2. fr_webpage/db_model/mysql.py 파일의 user, passwd, db를 local mysql의 id, pw, db_name로 변경해야함
3. face_recognition/attendance_check.py 파일 5번째 줄 database.database()의 파라미터를 local mysql의 id, pw, db_name로 
