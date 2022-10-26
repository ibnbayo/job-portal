from django.urls import path
from . views import api_list_view, api_detail_view, api_update_view,api_delete_view,api_create_user, JobAdvertListCreateView, JobAdvertListUpdateDeleteView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('adverts/', JobAdvertListCreateView.as_view()),
    path('adverts/<slug:slug>',JobAdvertListUpdateDeleteView.as_view()),
    path("", api_list_view, name="list"),
    path("<slug:slug>/", api_detail_view, name="jobdetail"),
    path("update/<slug:slug>", api_update_view, name="update2"),
    path("delete/<slug:slug>/", api_delete_view, name="delete2"),
    path("register/", api_create_user, name="register"),
    path("login", obtain_auth_token, name="login"),
]