from django.urls import path
from . views import api_list_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("list/", api_list_view, name="list"),
    path("login", obtain_auth_token, name="login"),
]