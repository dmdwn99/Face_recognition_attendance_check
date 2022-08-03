# Face_recognition_attendance_check

deepface모델을 pre-trained된 weights를 사용해서 face recognition을 진행합니다.\n\n\n\n\n

## 1. 모델이 얼굴을 인식하고 "cv2.error: OpenCV(4.6.0) /Users/runner/work/opencv-python/opencv-python/opencv/modules/imgproc/src/resize.cpp:4052: error: (-215:Assertion failed) !ssize.empty() in function 'resize'" error와 함께 종료.
-> 지속적으로 얼굴 인식할 수 있어야 함.

## 2. 현재 얼굴을 인식하면 "detected:  kdg1 ( 0.68989563 )" 이라고 출력됨. 
-> file명을 학번으로 해서 name, ID를 matching해서 return할 수 있도록 해야함. distance threshold가 <= 0.7로 default setting. 변경 
 
