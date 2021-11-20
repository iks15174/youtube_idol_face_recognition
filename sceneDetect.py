from scenedetect import VideoManager
from scenedetect import SceneManager

# For content-aware scene detection:
from scenedetect.detectors import ContentDetector
import pafy

SHOW_PROGRESS = True
FRAME_SKIP = 0

def find_scenes(video_path, threshold=30.0):
    # Create our video & scene managers, then add the detector.
    video_manager = VideoManager([video_path])
    scene_manager = SceneManager()
    scene_manager.add_detector(
        ContentDetector(threshold=threshold))

    # Improve processing speed by downscaling before processing.
    video_manager.set_downscale_factor()

    # Start the video manager and perform the scene detection.
    video_manager.start()
    scene_manager.detect_scenes(frame_source=video_manager, frame_skip=FRAME_SKIP, show_progress=SHOW_PROGRESS)

    # Each returned scene is a tuple of the (start, end) timecode.
    return scene_manager.get_scene_list()

videoUrl = input('youtube url : ')
video = pafy.new(videoUrl)
bestRes = video.getbest(preftype="mp4")
# videos = video.videostreams

# mp4Video = []
# for v in videos:
#     print(v.dimensions)
#     if v.extension == 'mp4':
#         mp4Video.append(v)
  
# quality = mp4Video[0].quality
# sortedMp4Video = sorted(mp4Video, key = lambda video : v.dimensions[0] * v.dimensions[1])
# for v in sortedMp4Video:
#     print(v.dimensions)
        

scenes = find_scenes(bestRes.url)
for scene in scenes:
    print(scene[0].get_timecode())