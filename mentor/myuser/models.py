from django.contrib.auth.models import User
from rest_framework import serializers, status

class UserSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'is_staff']


