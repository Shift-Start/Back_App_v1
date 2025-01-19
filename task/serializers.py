<<<<<<< HEAD
from rest_framework import serializers

from task.models import Task
class TaskSerializer(serializers.Serializer):
    task_id = serializers.CharField(read_only=True)  # التأكد من أنه نص
    user_id = serializers.CharField()  # التأكد من أنه نص
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    repetition = serializers.CharField()
    status = serializers.CharField()

    def create(self, validated_data):
        task_data = validated_data
        task = Task.create_task(task_data)  # استخدام الدالة لتخزين المهمة
        return task

    def to_representation(self, instance):
        """تحويل ObjectId إلى str في الاستجابة"""
        representation = super().to_representation(instance)
        
        # تحويل task_id و user_id إلى str
        representation['task_id'] = str(instance.get('task_id'))  # تحويل task_id إلى str
        representation['user_id'] = str(instance.get('user_id'))  # تحويل user_id إلى str
        
        return representation

=======
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

class TemplateTaskSerializer(serializers.Serializer):
    Templates = serializers.CharField(max_length=255)
    TaskID = serializers.CharField(max_length=255, required=True)
    Description = serializers.CharField(max_length=1000, required=False, allow_blank=True)
    TemplateID = serializers.CharField(max_length=255)
    StartDate = serializers.DateTimeField()
    EndDate = serializers.DateTimeField()
    Date = serializers.DateField()
    Point = serializers.FloatField()
    Status = serializers.CharField(max_length=50)
    Repetition = serializers.CharField(max_length=50)

class AddTemplateTaskSerializer(serializers.Serializer):
    TemplateID = serializers.CharField(max_length=24, required=True)  # ObjectId بطول 24 حرفًا
    TaskID = serializers.CharField(max_length=255, required=True)
    Description = serializers.CharField(max_length=1000, required=False, allow_blank=True)
    StartDate = serializers.DateTimeField(required=True)
    EndDate = serializers.DateTimeField(required=True)
    Date = serializers.DateField(required=True, input_formats=['%Y-%m-%d', '%d/%m/%Y', '%Y/%m/%d'])
    Point = serializers.FloatField(required=True)
    Status = serializers.CharField(max_length=50, required=True)
    Repetition = serializers.CharField(max_length=50, required=True)

    def validate_TemplateID(self, value):
        # التحقق من أن TemplateID صالح
        try:
            ObjectId(value)  # محاولة تحويل النص إلى ObjectId
        except Exception:
            raise serializers.ValidationError("Invalid TemplateID format.")
        return value
>>>>>>> f70151a67db44782b0182c41b22e35dbcd1ed815
