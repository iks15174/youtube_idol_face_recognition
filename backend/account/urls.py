from django.urls import path
from account.views import signin, signup, token, islogin

app_name = "account"

urlpatterns = [
    path("token/", token, name="token"),
    path("signin/", signin, name="signin"),
    path("signup/", signup, name="signup"),
    path("islogin/", islogin, name="islogin"),
]
