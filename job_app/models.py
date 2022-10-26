from email.policy import default
from django.db import models

# Create your models here.

class JobAdvert(models.Model):
    title = models.CharField(max_length = 200)
    company_name = models.CharField(max_length = 200)
    EMPLOYMENT_FULLTIME = 'F'
    EMPLOYMENT_CONTRACT = 'C'
    EMPLOYMENT_REMOTE = 'R'
    EMPLOYMENT_PARTTIME = 'P'
    EMPLOYMENT_CHOICES = [
        (EMPLOYMENT_FULLTIME, 'Full-time'),
        (EMPLOYMENT_CONTRACT, 'Contract'),
        (EMPLOYMENT_REMOTE, 'Remote'),
        (EMPLOYMENT_PARTTIME, 'Part-time')
    ]
    employment_type = models.CharField(max_length=1, choices=EMPLOYMENT_CHOICES, default = 'F')
    EXPERIENCE_ENTRY = 'E'
    EXPERIENCE_MID = 'M'
    EXPERIENCE_SENIOR = 'S'
    EXPERIENCE_CHOICES = [
        (EXPERIENCE_ENTRY, 'Entry level'),
        (EXPERIENCE_MID, 'Mid level'),
        (EXPERIENCE_SENIOR, 'Senior level')
    ]
    experience_level = models.CharField(max_length=1, choices=EXPERIENCE_CHOICES, default = 'E')
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_description = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)

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
    cover_letter = models.CharField(max_length=200, blank=True, null = True, default='N/A')
    job_advert = models.ForeignKey(JobAdvert, on_delete=models.CASCADE, default=1)


