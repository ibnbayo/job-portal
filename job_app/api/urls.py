from django.urls import path
from . views import adverts_api_list_view, adverts_api_detail_view, adverts_api_update_view,adverts_api_delete_view, adverts_api_create_user, applications_api_list_view, JobAdvertListCreateView, JobAdvertListUpdateDeleteView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('adverts/', JobAdvertListCreateView.as_view()),
    path('adverts/<slug:slug>',JobAdvertListUpdateDeleteView.as_view()),
    path("", adverts_api_list_view, name="list"),
    path("<slug:slug>/", adverts_api_detail_view, name="jobdetail"),
    path("update/<slug:slug>", adverts_api_update_view, name="update2"),
    path("delete/<slug:slug>/", adverts_api_delete_view, name="delete2"),
    path("register/", adverts_api_create_user, name="register"),
    path("applications/", applications_api_list_view, name="applications"),

    # path("<job_advert:job_advert>/applications/", applications_api_list_view, name="applist"),
    path("login", obtain_auth_token, name="login"),
]