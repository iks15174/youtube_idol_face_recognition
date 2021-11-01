import face_recognition
import cv2
import numpy as np
import pafy
def milToMinute(millis):
    seconds = (millis/1000)%60
    seconds = int(seconds)
    minutes = (millis/1000)/60
    minutes = int(minutes)
    return "{} : {}".format(minutes, seconds)

videoUrl = input('youtube url : ')
video = pafy.new(videoUrl)
bestRes = video.getbest(preftype="mp4")

vidcap = cv2.VideoCapture(bestRes.url)
print(vidcap)

jinImgae = face_recognition.load_image_file('./img/BTS_JIN.jfif')
jinFaceEncoding = face_recognition.face_encodings(jinImgae)[0]

jinminImgae = face_recognition.load_image_file('./img/BTS_JIMIN.jpg')
jinminFaceEncoding = face_recognition.face_encodings(jinminImgae)[0]

junggukImgae = face_recognition.load_image_file('./img/BTS_JUNGGUK.jfif')
junggukFaceEncoding = face_recognition.face_encodings(junggukImgae)[0]

sugarImgae = face_recognition.load_image_file('./img/BTS_SUGAR.jpg')
sugarFaceEncoding = face_recognition.face_encodings(sugarImgae)[0]

vImgae = face_recognition.load_image_file('./img/BTS_V.jfif')
vFaceEncoding = face_recognition.face_encodings(vImgae)[0]

knownFaceEncoding = [jinFaceEncoding, jinminFaceEncoding, junggukFaceEncoding, sugarFaceEncoding, vFaceEncoding]
knownFaceName = ["JIN", "jimin", "jungguk", 'sugar', 'v']

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    frameExist, frame = vidcap.read()
    time = 0
    if frameExist:
        time = vidcap.get(cv2.CAP_PROP_POS_MSEC)

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        # print(face_locations)
        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(knownFaceEncoding, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(knownFaceEncoding, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = knownFaceName[best_match_index]
                if name == 'JIN':
                    print(milToMinute(time))

            face_names.append(name)

    process_this_frame = not process_this_frame

