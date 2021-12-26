from django.urls import path
from django.contrib.auth import views as auth_views
from account.views import signin, signup, token

app_name = "account"

urlpatterns = [
    path("token/", token, name="token"),
    path("signin/", signin, name="signin"),
    path("signup/", signup, name="signup"),
]
