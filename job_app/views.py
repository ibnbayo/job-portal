from django.shortcuts import render
from . models import JobAdvert, JobApplication
# Create your views here.
def home(request):
    adverts = JobAdvert.objects.all()
    return render(request, "job_app/index.html", {"adverts": adverts})

def applications(request):
    applications = JobApplication.objects.all()
    return render(request, "job_app/applications.html", {"applications": applications})