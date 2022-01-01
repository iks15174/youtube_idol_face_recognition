from backend.faceimage.faceDetect.video.videoInterface import VideoInterface
from pytube import YouTube
import cv2


class YoutubeVideo(VideoInterface):
    def __init__(self):
        self.src = None

    def get_video_src(self):
        return self.src

    def parse(self, path):
        yt = YouTube(path)
        self.src = cv2.VideoCapture(
            yt.streams.filter(file_extension="mp4")
            .order_by("resolution")
            .desc()
            .first()
            .url
        )
