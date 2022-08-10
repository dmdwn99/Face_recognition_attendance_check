##2022-08-09
1. deepface 모델 성능 확인
2. 프로젝트 전체 구조 수정: APP, DB, DL_MODEL 등의 폴더 구조를 face_recognition, attendance_check로 재구성
3. DB를 Mysql로 하여 user_check table의 check 값 변경, 학번과 현재 날짜를 기준으로 하였음
4. deepface를 실행하면 deepface에서 인식한 사람을 attendance_check 모듈에서 DB 변경
5. 모델 작동은 되는데 사람 인식이 되지 않음