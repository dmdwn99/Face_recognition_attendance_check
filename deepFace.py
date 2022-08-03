from deepface import DeepFace


# img1_path = 'imagebasic/kdg1.jpg'
# img2_path = 'imagebasic/kdg2.jpg'
#
# result = DeepFace.verify(img1_path = "imagebasic/kdg1.jpg", img2_path = "imagebasic/kdg2.jpg")
# print(result)
#
# obj = DeepFace.analyze(img_path = "imagebasic/kdg1.jpg", actions = ['age', 'gender'])
# print(obj)

DeepFace.stream('imagebasic',model_name='DeepFace')