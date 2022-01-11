from pytube import YouTube
import os
import shutil
import cv2

TEMP_FILE_PATH = "./videos/"
FILE_NAME = "video.mp4"


class YoutubeToVideo:
    def __init__(self):
        self.video_path = ""

    def get_video_cap(self):
        print(self.video_path + "/" + FILE_NAME)
        return cv2.VideoCapture(self.video_path + "/" + FILE_NAME)

    def download(self, link):
        print("----start download youtube video----")
        yt = YouTube(link)
        self.video_path = YoutubeToVideo.get_file_name()
        yt.streams.filter(progressive=True, file_extension="mp4").order_by(
            "resolution"
        ).desc().first().download(output_path=self.video_path, filename=FILE_NAME)
        print("----finish download youtube video----")
        return self

    def delete(self):
        shutil.rmtree(self.video_path)

    @staticmethod
    def get_file_name():
        dir_num = 0
        while True:
            if os.path.exists(TEMP_FILE_PATH + str(dir_num)):
                dir_num += 1
            else:
                os.makedirs(TEMP_FILE_PATH + str(dir_num))
                return TEMP_FILE_PATH + str(dir_num)
