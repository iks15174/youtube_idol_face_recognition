from json.decoder import JSONDecodeError
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.http.response import HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
import json
from faceimage.faceDetect.core import FaceDetect
from faceimage.faceDetect.video.youtubeToVideo import YoutubeToVideo
from background_task import background
from faceimage.models import FaceDetectJob, ImageGroup, Image
from commonUtil.login_required import login_required
from datetime import datetime

FILE_TYPE = 10
LINK_TYPE = 11


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
        image_group = ImageGroup.objects.create(
            user=user,
            name=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            + youtube_video.get_video_name,
        )
        face_detect_job.finished = True
        face_detect_job.image_group = image_group
        face_detect_job.save()

    finally:
        youtube_video.delete()


@login_required
@require_http_methods(["GET"])
def jobs(request):
    return JsonResponse(
        list(FaceDetectJob.objects.filter(user=request.user)), safe=False
    )


@login_required
@require_http_methods(["GET", "POST"])
def folders(request):
    if request.method == "GET":
        parent_id = request.GET.get("parent", None)
        if parent_id:
            parent = get_object_or_404(ImageGroup, id=parent_id)
            parent_dic = model_to_dict(parent)
        else:
            parent = None
            parent_dic = ""
        image_groups = list(
            ImageGroup.objects.filter(parent=parent, user=request.user).values(
                "name", "parent"
            )
        )

        return JsonResponse(
            {"parent": parent_dic, "folders": image_groups}, safe=False, status=200
        )

    # POST 요청이 들어왔을 경우
    try:
        req_data = json.loads(request.body.decode())
        parent_id = req_data["parent"]
        folder_name = req_data["name"]
        parent = get_object_or_404(ImageGroup, id=parent_id)
        new_image_group = ImageGroup.objects.create(
            name=folder_name, user=request.user, parent=parent
        )
        return JsonResponse(model_to_dict(new_image_group), safe=False)

    except (KeyError, JSONDecodeError):
        return HttpResponseBadRequest()


@login_required
@require_http_methods(["GET"])
def jobs(request):
    my_face_detect_jobs = list(
        FaceDetectJob.objects.filter(user=request.user).values(
            "id",
            "name",
            "image_group__id",
            "finished",
            "created_at",
            "finished_at",
            "link",
        )
    )
    return JsonResponse(my_face_detect_jobs, safe=False)
