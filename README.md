# Face_recognition_attendance_check
07/31
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
  ![화면 캡처 2022-07-31 192835](https://user-images.githubusercontent.com/77705600/182021985-d69642fc-42b9-45f1-900b-a7e5bfbf045d.png)
