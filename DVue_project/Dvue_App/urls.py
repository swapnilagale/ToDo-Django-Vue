from django.contrib import admin
from django.urls import path
from .views import Taskviewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'tasks',Taskviewset)
