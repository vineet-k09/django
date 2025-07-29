from rest_framework import serializers
from .models import TaskBoard

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskBoard
        fields = '_all_'