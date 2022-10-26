from rest_framework import serializers

from job_app.models import JobAdvert
from account.models import CustomUser

class JobAdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobAdvert
        fields = ['title','company_name','employment_type','experience_level','description','location','job_description']

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