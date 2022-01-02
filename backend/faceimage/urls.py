from django.urls import path
from faceimage.views import get_face

app_name = "faceimage"

urlpatterns = [
    path("get-face/", get_face, name="get_face"),
]
