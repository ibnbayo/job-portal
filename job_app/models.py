from email.policy import default
from django.db import models
from django.urls import reverse
# from django.db.models import CharField, Model
from autoslug import AutoSlugField


# Create your models here.

class JobAdvert(models.Model):
    title = models.CharField(max_length = 200)
    company_name = models.CharField(max_length = 200)
    EMPLOYMENT_FULLTIME = 'Full'
    EMPLOYMENT_CONTRACT = 'Contract'
    EMPLOYMENT_REMOTE = 'Remote'
    EMPLOYMENT_PARTTIME = 'Part'
    EMPLOYMENT_CHOICES = [
        (EMPLOYMENT_FULLTIME, 'Full-time'),
        (EMPLOYMENT_CONTRACT, 'Contract'),
        (EMPLOYMENT_REMOTE, 'Remote'),
        (EMPLOYMENT_PARTTIME, 'Part-time')
    ]
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_CHOICES, default = 'Full-time')
    EXPERIENCE_ENTRY = 'Entry'
    EXPERIENCE_MID = 'Mid'
    EXPERIENCE_SENIOR = 'Senior'
    EXPERIENCE_CHOICES = [
        (EXPERIENCE_ENTRY, 'Entry level'),
        (EXPERIENCE_MID, 'Mid level'),
        (EXPERIENCE_SENIOR, 'Senior level')
    ]
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default = 'Entry')
    STATUS = (('unpublished','Unpublushed'),
                ('published','Published'))
    status = models.CharField(max_length=50, choices=STATUS, default="published")
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_description = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='title')
    # slug = models.SlugField(default='job')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("advert_detail", kwargs={"slug": self.slug})


class JobApplication(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    linkedin_url = models.URLField(max_length=100)
    github_url = models.URLField(max_length=100)
    website = models.CharField(max_length=200, blank=True, null=True, default='N/A')
    EXPERIENCE_ZERO = '0'
    EXPERIENCE_ONE = '1'
    EXPERIENCE_THREE = '3'
    EXPERIENCE_FIVE = '5'
    EXPERIENCE_SEVEN = '7'
    EXPERIENCE_YEARS_CHOICES = [
        (EXPERIENCE_ZERO, '0-1'),
        (EXPERIENCE_ONE, '1-2'),
        (EXPERIENCE_THREE, '3-4'),
        (EXPERIENCE_FIVE, '5-6'),
        (EXPERIENCE_SEVEN, '7 and above'),
    ]
    years_of_experience = models.CharField(max_length=1, choices=EXPERIENCE_YEARS_CHOICES, default='0')
    cover_letter = models.TextField(max_length=200, blank=True, null = True, default='N/A')
    #The related_name attribute specifies the name of the reverse relation from the User model back to your model.
    job_advert = models.ForeignKey(JobAdvert, related_name='applications', on_delete=models.CASCADE, default=1)
    date_added = models.DateTimeField(auto_now=True)


