from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import Task

class TaskSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Task
        fields=('id','description','status')
