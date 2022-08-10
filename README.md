# Face_recognition_attendance_check
---
- 얼굴 검출하여 다른 폴더에 저장하는 OpenCV 모델
  - deepface의 기능을 아직 잘 몰라 OpenCV로 만듦
  
  ~~~ py
  # https://github.com/opencv/opencv/tree/master/samples/dnn/face_detector
  # SSD 방식 기반의 얼굴 검출
  model = 'opencv_face_detector/res10_300x300_ssd_iter_140000_fp16.caffemodel'
  config = 'opencv_face_detector/deploy.prototxt'
  ~~~
  
  ~~~ py
  blob = cv2.dnn.blobFromImage(frame, 1, (300, 300), (104, 177, 123))
  net.setInput(blob)
  
  detect = net.forward()
  detect = detect[0,0,:,:]
  # detect.shape = (1, 1, N, 7)이고, 이 중 뒤쪽 두개의 차원에 검출 정보가 저장됨.
  # 편의상 2차원 행렬로 변환하여 사용
  ~~~
  
---
sqlite3/mongoDB 이용한 DB생성
- 모델이 local에서 돌아가는게 빡빡해서 colab으로 이용
- 모델이랑 db 생성은 되는듯
- 
~~~ py
# colab
import sqlite3

# DB 생성, 오토 커밋
conn = sqlite3.connect('student.db')

# 커서 획득
cursor = conn.cursor()

# Creating database tables
cursor.execute("CREATE TABLE Student_Attendance (id integer PRIMARY KEY, attendance text)")

# 모델 들어갈 자리
# 모델에서 학번 반환하고 pandas dataframe 만들기

for index, instance in tqdm(df.iterrows(), total=df.shape[0]):
    # df = 모델에서 반환한 ID 값을 저장한 데이터프레임
    #img_name = instance['img_name']
    ID = instance['ID'] # 학번만 반환한다면 이거만 쓰면 됨

    insert_statement = 'INSERT INTO Student_Attendance (ID) VALUES (?)'
    insert_args = (index, ID)
    cursor.execute(insert_statement, insert_args)

conn.commit()
~~~
