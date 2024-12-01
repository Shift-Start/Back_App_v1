from rest_framework import serializers

from login.models import Task
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

