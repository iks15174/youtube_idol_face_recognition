from django.urls import path
from django.contrib.auth import views as auth_views
from account.views import signin, signup

app_name = "account"

urlpatterns = [
    path("signin/", signin, name="signin"),
    path("signup/", signup, name="signup"),
]
