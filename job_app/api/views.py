from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from job_app.models import JobAdvert
from . serializers import JobAdvertSerializer
from django.contrib.auth.models import User

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter

@api_view(["GET","POST"])
def api_list_view(request):
    if request.method == "GET":
        adverts = JobAdvert.objects.all()
        serializer = JobAdvertSerializer(adverts, many = True)
        return Response(serializer.data)

    elif request.method == "POST":
        user = User.objects.get(pk=1)
        advert = JobAdvert(author=user)

        serializer = JobAdvertSerializer(advert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # queryset = JobAdvert.objects.all()
    # print(queryset)
    # serializer = JobAdvertSerializer(queryset, many=True)
    # return Response(serializer.data)

def login(request):
    username = request.POST['username']