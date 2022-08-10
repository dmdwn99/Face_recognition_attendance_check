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
