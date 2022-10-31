from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from job_app.models import JobAdvert, JobApplication
from . serializers import JobAdvertSerializer, JobApplicationSerializer, UserRegistrationSerializer
from account.models import CustomUser

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter

from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method="post", request_body=JobAdvertSerializer())
@api_view(["GET","POST"])
def adverts_api_list_view(request):
    if request.method == "GET":
        adverts = JobAdvert.objects.all()
        serializer = JobAdvertSerializer(adverts, many = True)
        return Response(serializer.data)

    elif request.method == "POST":
        user = CustomUser.objects.get(pk=1)
        advert = JobAdvert()
        # advert = JobAdvert(author=user)

        serializer = JobAdvertSerializer(advert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # queryset = JobAdvert.objects.all()
    # print(queryset)
    # serializer = JobAdvertSerializer(queryset, many=True)
    # return Response(serializer.data)

@api_view(["GET"])
def adverts_api_detail_view(request, slug):
    try:
        advert = JobAdvert.objects.get(slug=slug)
    except JobAdvert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = JobAdvertSerializer(advert)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def adverts_api_update_view(request, slug):
    try:
        advert = JobAdvert.objects.filter(slug=slug).first()
    except JobAdvert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = JobAdvertSerializer(advert, data=request.data)
        #For post and put, u need to check if its valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def adverts_api_delete_view(request, slug):
    try:
        advert = JobAdvert.objects.get(slug=slug)
    except JobAdvert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = advert.delete()
        data = {}
        if operation:
            data['Success'] = 'Post deleted successfully!'
        else:
            data['Failure'] = 'Post deletion failed'
        return Response(data=data)

@api_view(['POST'])
def adverts_api_create_user(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            data = {}
            user = serializer.save()
            data['Suceess'] = 'User creation successful!'
            data['username'] = user.username
            data['email'] = user.email
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobAdvertListCreateView(ListCreateAPIView):
    '''
    Use this view to create
    '''
    queryset = JobAdvert.objects.all()
    serializer_class = JobAdvertSerializer


    pagination_class  = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['title', 'content', 'slug', 'author__username']

class JobAdvertListUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    '''
    Use this view to read, update, delete
    '''
    queryset = JobAdvert.objects.all()
    lookup_field = 'slug'
    serializer_class = JobAdvertSerializer

@api_view(["GET","POST"])
def applications_api_list_view(request, job_advert):
    if request.method == "GET":
        applications = JobApplication.objects.get(job_advert=job_advert)
        serializer = JobApplicationSerializer(applications, many = True)
        return Response(serializer.data)

    elif request.method == "POST":
        user = CustomUser.objects.get(pk=1)
        application = JobApplication(author=user)

        serializer = JobApplicationSerializer(application, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def login(request):
    username = request.POST['username']