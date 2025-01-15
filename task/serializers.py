from datetime import datetime
from rest_framework import serializers
from bson import ObjectId

class TaskSerializer(serializers.Serializer):
    TaskID = serializers.CharField(max_length=50, required=False)
    UserID = serializers.CharField(max_length=24,required=True)
    Title = serializers.CharField(max_length=200, required=True)
    Description = serializers.CharField(max_length=500, allow_blank=True, required=False)
    Date = serializers.DateTimeField(required=True)  # تاريخ المهمة
    StartDate = serializers.DateTimeField(required=True)  # تاريخ البدء
    EndDate = serializers.DateTimeField(required=True)  # تاريخ الانتهاء
    repetition = serializers.CharField(max_length=50, required=False, allow_blank=True)
    Status = serializers.CharField(max_length=50, required=True)  # حالة المهمة

class TemplateSerializer(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=1024)
    CreatedAt = serializers.DateTimeField(read_only=True)