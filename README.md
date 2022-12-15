# Job Portal
[![Screenshot-2022-12-15-at-16-19-17.png](https://i.postimg.cc/KYMcYBsM/Screenshot-2022-12-15-at-16-19-17.png)](https://postimg.cc/v1GwqgyY)

## Overview
Job Portal API featuring job adverts and applications.
Live Link: [jobs-portal.up.railway.app/docs/]


## Features

### Job Advert
- Title
- Company name
- Employment type (full-time, contract, remote, part-time)
- Experience level ( Entry level, Mid-level, Senior)
- Description
- Location
- Job description

### Job Application
- First name
- Last name
- Email address
- Phone
- Linkedin profile URL
- GitHub profile URL
- Website (optional)
- Years of experience (0 - 1, 1 - 2, 3 - 4, 5 - 6, 7 and above)
- Cover letter (Should be optional and can be a CharField)

### User
- Username or email
- password

### Specifications
- API endpoint to login and logout users 
- API endpoint that returns a list of Job adverts in the DB. 
- API endpoint that retrieves the detail of a job advert
- API endpoint to update a Job Advert
- API endpoint to delete a Job Advert
- API endpoint to publish and unpublish a Job Advert.
- API endpoint that retrieves all the job applications that belong to a job advert
- API endpoint that retrieves a single Job Application
- API endpoint to submit a Job application for a job advert
- API endpoint to delete a Job Application

### Requirements
- Users signup and activate their account
- Job Advert can only be deleted only after it has been unpublished
- Job Advert can be published and unpublished.
- Job Applications can only be submitted for job adverts that has been published.
- All database queries made with Django ORM.


## Technologies 
- Django
- REST Framework
- Oauthlib


## Running The Project
Live version:
[Job Portal](jobs-portal.up.railway.app/docs/)

From the repo:<br/>
  - Clone this project locally<br/>
  - Install dependencies from requirements.txt<br/>
  - python manage.py runserver<br/>

## To Do
- Add applicant count and publish status to job advert response. Published adverts should come first followed by
adverts with the highest applicant count and then recently created adverts.
- Allow guest users access to only published job adverts.

