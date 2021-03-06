import face_recognition
import cv2
import numpy as np
import pafy
from faceDetect import face_detection


def milToMinute(millis):
    seconds = (millis / 1000) % 60
    seconds = int(seconds)
    minutes = (millis / 1000) / 60
    minutes = int(minutes)
    return "{} : {}".format(minutes, seconds)


def drawBox(top, right, bottom, left, frame, name=""):
    top *= 4
    right *= 4
    bottom *= 4
    left *= 4

    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    return frame


videoUrl = input("youtube url : ")
video = pafy.new(videoUrl)
bestRes = video.getbest(preftype="mp4")

vidcap = cv2.VideoCapture(bestRes.url)

jinImgae = face_recognition.load_image_file("./img/BTS_JIN.jpg")
jinFaceEncoding = face_recognition.face_encodings(jinImgae)[0]

jinminImgae = face_recognition.load_image_file("./img/BTS_JIMIN.jpg")
jinminFaceEncoding = face_recognition.face_encodings(jinminImgae)[0]

junggukImgae = face_recognition.load_image_file("./img/BTS_JUNGGUK.jpg")
junggukFaceEncoding = face_recognition.face_encodings(junggukImgae)[0]

sugarImgae = face_recognition.load_image_file("./img/BTS_SUGAR.jpg")
sugarFaceEncoding = face_recognition.face_encodings(sugarImgae)[0]

vImgae = face_recognition.load_image_file("./img/BTS_V.jpg")
vFaceEncoding = face_recognition.face_encodings(vImgae)[0]

jihyoImgae = face_recognition.load_image_file("./faceDetection/30.jpg")
jihyoFaceEncoding = face_recognition.face_encodings(jihyoImgae)[0]

# knownFaceEncoding = [jinFaceEncoding, jinminFaceEncoding, junggukFaceEncoding, sugarFaceEncoding, vFaceEncoding]
# knownFaceName = ["JIN", "jimin", "jungguk", 'sugar', 'v']

knownFaceEncoding = [jihyoFaceEncoding]
knownFaceName = ["JIHYO"]


face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    frameExist, frame = vidcap.read()
    time = 0
    if not frameExist:
        break

    time = vidcap.get(cv2.CAP_PROP_POS_MSEC)

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_detection(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations
        )

        for (top, right, bottom, left) in face_locations:
            drawBox(top, right, bottom, left, frame)

        for idx, face_encoding in enumerate(face_encodings):
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(knownFaceEncoding, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(
                knownFaceEncoding, face_encoding
            )
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = knownFaceName[best_match_index]
                if name == "JIHYO":
                    print(face_locations[idx])
                    (top, right, bottom, left) = face_locations[idx]
                    drawBox(top, right, bottom, left, frame, "??????")
                    print(milToMinute(time))

    cv2.imshow("frame", frame)
    key = cv2.waitKey(25)

    process_this_frame = not process_this_frame
