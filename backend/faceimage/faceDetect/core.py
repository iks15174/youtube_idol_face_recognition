import cv2
import pafy
import numpy as np
from faceimage.models import Image


class FaceDetect:
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    def __init__(self, video_src, user):
        self.count = 0
        self.face_occur_threshold = 20
        self.video_src = video_src
        self.user = user

    def save_face_image(self, frame, location):
        print("sace_face_image called")
        # global IMG_COUNT
        # (x, y, w, h) = location
        # face = frame[y : y + h, x : x + w]  # slice the face from the image
        # cv2.imwrite(
        #     FACE_DETECT_SAVE_FOLDER + str(IMG_COUNT) + ".jpg", face
        # )  # save the image
        # IMG_COUNT += 1

    @classmethod
    def face_detection(cls, frame):
        # Read the image
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detect faces in the image
        faces = cls.face_cascade.detectMultiScale(
            frame,
            scaleFactor=1.05,  # 이미지에서 얼굴 크기가 서로 다른 것을 보상해주는 값
            minNeighbors=5,  # 얼굴 사이의 최소 간격(픽셀)입니다
            minSize=(10, 10),  # 얼굴의 최소 크기입니다
        )
        # 검출된 얼굴 주변에 사각형 그리기
        # for (x, y, w, h) in faces:
        #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # face recognition 적용을 위한 변환
        for face in faces:
            top = face[1]
            left = face[0]
            right = face[0] + face[2]
            bottom = face[1] + face[3]
            face[0] = top
            face[1] = right
            face[2] = bottom
            face[3] = left
        return faces

    @staticmethod
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

    def run(self):
        print("Face detection started")
        saved_locs = []
        prev_face_locations = []
        while True:
            frameExist, frame = self.video_src.read()
            if not frameExist:
                print("Frame doesn't exist")
                break

            cur_face_locations = FaceDetect.face_detection(frame)
            FaceDetect.find_similiar_location(
                prev_face_locations, cur_face_locations, saved_locs, 10
            )
            prev_face_locations = cur_face_locations

            for index, saved_loc in enumerate(saved_locs):
                if saved_loc["count"] >= self.face_occur_threshold:
                    self.save_face_image(frame, saved_loc["location"])
                    del saved_locs[index]
                    print(
                        f"Face occured over {self.face_occur_threshold} saved in Model"
                    )

        self.video_src.release()
        cv2.destroyAllWindows()
