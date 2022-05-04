import imp
from multiprocessing import AuthenticationError
from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializers

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class Taskviewset(viewsets.ModelViewSet):
    authentication_classes=(BasicAuthentication,)
    permission_classes=(IsAuthenticated,)
    queryset=Task.objects.all()
    serializer_class=TaskSerializers