from json.decoder import JSONDecodeError
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.http.response import Http404, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
import json
from faceimage.faceDetect.core import FaceDetect
from faceimage.faceDetect.video.youtubeToVideo import YoutubeToVideo
from background_task import background
from faceimage.models import FaceDetectJob, ImageGroup, Image
from commonUtil import login_required
from datetime import datetime

FILE_TYPE = 10
LINK_TYPE = 11


def get_root_folder(user):
    return ImageGroup.objects.get(user=user, parent=None)


@login_required
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
        youtube_video = YoutubeToVideo(link)

        youtube_src = youtube_video.download().get_video_cap()
        FaceDetect(youtube_src, user).run()
        face_detect_job.finished = True
        face_detect_job.save()
        ImageGroup.objects.create(
            user=user,
            name=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            + youtube_video.get_video_name,
        )

    finally:
        youtube_video.delete()


@login_required
@require_http_methods(["GET", "POST"])
def folders(request):
    if request.method == "GET":
        try:
            req_data = json.loads(request.body.decode())
            src_type = req_data["type"]
        except (KeyError, JSONDecodeError):
            return HttpResponseBadRequest()
    print(get_root_folder(request.user).name)
    return HttpResponse(status=201)


@login_required
@require_http_methods(["GET"])
def jobs(request):
    my_face_detect_jobs = FaceDetectJob.objects.filter(user=request.user).values(
        "finished", "created_at", "finished_at"
    )
    return JsonResponse(my_face_detect_jobs, safe=False)
