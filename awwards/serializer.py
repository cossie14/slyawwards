from rest_framework import serializers
from .models import Profile,Project

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'post', 'pub_date','project_pic')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'username', 'contact', 'bio','profile_picture','user_id')
