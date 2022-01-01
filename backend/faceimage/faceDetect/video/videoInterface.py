import abc


class VideoInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_video_src(self):
        pass

    @abc.abstractmethod
    def parse(self, path):
        pass
