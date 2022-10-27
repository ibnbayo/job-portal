from rest_framework import serializers

from job_app.models import JobAdvert, JobApplication
from account.models import CustomUser

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['first_name','last_name','email','phone','linkedin_url','github_url','website','years_of_experience','cover_letter','job_advert']

class JobAdvertSerializer(serializers.ModelSerializer):
    job_applications = JobApplicationSerializer(many=True, source='job_application_set') 

    class Meta:
        model = JobAdvert
        fields = '__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['username','email','password','password2']
        extra_kwargs = {
        'password': {'write_only':True}
        }

    

    def save(self):
        user = CustomUser(
            email = self.validated_data['email'],
            username = self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'Response': 'Both passwords dont match'})
        user.set_password(password)
        user.save()
        return user