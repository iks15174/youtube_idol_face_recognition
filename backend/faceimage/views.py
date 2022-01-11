from json.decoder import JSONDecodeError
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.http.response import Http404, HttpResponseBadRequest
from django.contrib.auth import authenticate, get_user_model, login
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
import json
from faceimage.faceDetect.core import FaceDetect
from faceimage.faceDetect.video.youtubeToVideo import YoutubeToVideo
from background_task import background
from faceimage.models import FaceDetectJob, ImageGroup, Image

FILE_TYPE = 10
LINK_TYPE = 11


def get_root_folder(user):
    return ImageGroup.objects.get(user=user, parent=None)


@require_http_methods(["POST"])
def get_face(request):
    try:
        req_data = json.loads(request.body.decode())
        src_type = req_data["type"]
        face_detect_job = FaceDetectJob.objects.create(user=request.user)
        if src_type == LINK_TYPE:
            link = req_data["link"]
            get_face_background(request.user.id, link, face_detect_job.id)
            return HttpResponse(status=201)
        elif src_type == FILE_TYPE:
            file = request.FILES
        else:
            face_detect_job.delete()
            return HttpResponseBadRequest()
    except (KeyError, JSONDecodeError):
        face_detect_job.delete()
        return HttpResponseBadRequest()


@background(schedule=60)
def get_face_background(user_id, link, face_detect_job_id):
    try:
        user = User.objects.get(id=user_id)
        face_detect_job = FaceDetectJob.objects.get(id=face_detect_job_id)
        youtube_video = YoutubeToVideo()

        youtube_src = youtube_video.download(link).get_video_cap()
        FaceDetect(youtube_src, user).run()
        face_detect_job.finished = True
        face_detect_job.save()
    finally:
        youtube_video.delete()


@require_http_methods(["GET", "POST"])
def folders(request):
    print(get_root_folder(request.user).name)
    return HttpResponse(status=201)
