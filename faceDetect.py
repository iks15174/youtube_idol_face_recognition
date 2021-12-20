import cv2
from datetime import datetime
import pafy


cascPath = "face_detect.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
img_path = "img/face_detect_ex1.webp"

videoUrl = input("youtube url : ")
video = pafy.new(videoUrl)
bestRes = video.getbest(preftype="mp4")
vidcap = cv2.VideoCapture(bestRes.url)


def face_detection(frame):
    iteration_count = 10
    for cnt in range(0, iteration_count):

        # Read the image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,  # 이미지에서 얼굴 크기가 서로 다른 것을 보상해주는 값
            minNeighbors=5,  # 얼굴 사이의 최소 간격(픽셀)입니다
            minSize=(30, 30),  # 얼굴의 최소 크기입니다
        )

        # 검출된 얼굴 주변에 사각형 그리기
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


# while True:
#     frameExist, frame = vidcap.read()
#     if not frameExist:
#         break

#     big_frame = cv2.resize(frame, (0, 0), fx=1.5, fy=1.5)
#     face_detection(big_frame)

#     cv2.imshow("frame", big_frame)
#     key = cv2.waitKey(25)
img = cv2.imread(img_path)
face_detection(img)
cv2.imshow("Face detected", img)
