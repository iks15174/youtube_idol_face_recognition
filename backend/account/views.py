from json.decoder import JSONDecodeError
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.http.response import HttpResponseBadRequest
from django.contrib.auth import authenticate, get_user_model, login
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
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

    UserModel.objects.create_user(email=email, password=password, nickname=nick_name)
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
