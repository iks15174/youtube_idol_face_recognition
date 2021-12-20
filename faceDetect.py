import cv2
import pafy
import numpy as np


FACE_OCCUR_TRHESHOLD = 20
faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


def face_detection(frame):
    # Read the image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.05,  # 이미지에서 얼굴 크기가 서로 다른 것을 보상해주는 값
        minNeighbors=5,  # 얼굴 사이의 최소 간격(픽셀)입니다
        minSize=(10, 10),  # 얼굴의 최소 크기입니다
    )
    # 검출된 얼굴 주변에 사각형 그리기
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    return faces


def find_similiar_location(prev_locs, cur_locs, saved_locs, error=10):
    if len(cur_locs) == 0:
        return

    added_cur_loc_indexes = []

    # 이전의 location과 유사한 현재의 loc을 찾아 saved_locs의 등장횟수(count)를 증가시킨다.
    for prev_loc in prev_locs:
        for index, cur_loc in enumerate(cur_locs):
            if (
                abs(cur_loc[0] - prev_loc[0]) < error
                and abs(cur_loc[1] - prev_loc[1]) < error
                and abs(cur_loc[2] - prev_loc[2]) < error
                and abs(cur_loc[3] - prev_loc[3]) < error
            ):
                for saved_loc in saved_locs:
                    if np.array_equal(saved_loc["location"], prev_loc):
                        saved_loc["location"] = cur_loc
                        saved_loc["count"] += 1
                        saved_loc["new"] = True
                        added_cur_loc_indexes.append(index)

    # 업데이트 되지 않은 prev location들은 saved_locs에서 삭제한다.
    for index, saved_loc in enumerate(saved_locs):
        if saved_loc["new"] == False:
            del saved_locs[index]

    # 새롭게 등장한 cur location들을 saved_locs에 추가한다.
    for index, cur_loc in enumerate(cur_locs):
        if not index in added_cur_loc_indexes:
            saved_locs.append({"location": cur_loc, "count": 0, "new": False})

    for saved_loc in saved_locs:
        saved_loc["new"] = False


def img_test():
    img_path = "img/face_detect_ex1.webp"
    img = cv2.imread(img_path)
    face_detection(img)
    cv2.imshow("Face detected", img)
    cv2.waitKey(0)


def youtube_test():
    videoUrl = input("youtube url : ")
    video = pafy.new(videoUrl)
    bestRes = video.getbest(preftype="mp4")
    vidcap = cv2.VideoCapture(bestRes.url)

    saved_locs = []
    prev_face_locations = []
    while True:
        frameExist, frame = vidcap.read()
        if not frameExist:
            break

        cur_face_locations = face_detection(frame)
        find_similiar_location(prev_face_locations, cur_face_locations, saved_locs, 10)
        prev_face_locations = cur_face_locations

        for index, saved_loc in enumerate(saved_locs):
            if saved_loc["count"] >= FACE_OCCUR_TRHESHOLD:
                print(saved_loc)
                del saved_locs[index]
                print(f"Face detected in postion")

        cv2.imshow("frame", frame)
        key = cv2.waitKey(25)


youtube_test()
