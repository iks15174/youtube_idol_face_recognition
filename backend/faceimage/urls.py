from django.urls import path
from faceimage.views import get_face, folders

app_name = "faceimage"

urlpatterns = [
    path("faces/", get_face, name="get_face"),
    path("folders/", folders, name="folders"),
]
