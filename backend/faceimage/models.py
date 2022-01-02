from django.db import models
from django.contrib.auth import get_user_model
import datetime


# Create your models here.
MyUser = get_user_model()


class FaceDetectJob(models.Model):
    user = models.ForeignKey(
        MyUser, related_name="face_detect_jobs", on_delete=models.CASCADE
    )
    finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True)

    # finished되면 끝난 시간을 함께 저장해준다.
    def save(self, *args, **kwargs):
        if self.finished:
            self.finished_at = datetime.datetime.now()

        super().save(*args, **kwargs)


class ImageGroup(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(
        MyUser, related_name="image_groups", on_delete=models.CASCADE
    )
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    user = models.ForeignKey(MyUser, related_name="images", on_delete=models.CASCADE)
    image_group = models.ForeignKey(
        ImageGroup, related_name="images", on_delete=models.CASCADE
    )
