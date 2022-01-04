from json.decoder import JSONDecodeError
from django.http import HttpResponse
from django.http.response import HttpResponseBadRequest
from django.contrib.auth import authenticate, get_user_model, login
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie
from faceimage.models import ImageGroup
import json


UserModel = get_user_model()


@ensure_csrf_cookie
@require_http_methods(["GET"])
def token(request):
    return HttpResponse(status=204)


@require_http_methods(["POST"])
@ensure_csrf_cookie
def signup(request):
    try:
        req_data = json.loads(request.body.decode())
        email = req_data["email"]
        password = req_data["password"]
        nick_name = req_data["nickName"]
    except (KeyError, JSONDecodeError):
        return HttpResponseBadRequest()

    user = UserModel.objects.create_user(
        email=email, password=password, nickname=nick_name
    )
    ImageGroup.objects.create(user=user, name=user.nickname)
    return HttpResponse(status=201)


@require_http_methods(["POST"])
@ensure_csrf_cookie
def signin(request):
    req_data = json.loads(request.body.decode())
    email = req_data["email"]
    password = req_data["password"]
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse(status=204)
    return HttpResponse(status=401)


@require_http_methods(["GET"])
@ensure_csrf_cookie
def islogin(request):
    if request.user.is_authenticated:
        return HttpResponse(status=204)
    return HttpResponse(status=401)
