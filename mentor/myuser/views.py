from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from rest_framework import viewsets, permissions, status

from django.contrib.auth.models import User

from myuser.models import UserSerializer

from rest_framework.permissions import BasePermission


class CreatorOnly(BasePermission):
    def has_permission(self, request, view):
        print("-----------------------")
        if request.user.groups.filter(name='buyer').exists():
            if request.method in ['GET']:
                return True
            else:
                return False
        return True


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CreatorOnly]

    def perform_create(self, serializer):
        if 'password' in self.request.data:
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()
