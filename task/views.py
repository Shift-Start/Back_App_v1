from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from login.models import Task  # استيراد موديل Task
from task.serializers import TaskSerializer  # استيراد Serializers الخاص بالمهمة
from bson import json_util
from rest_framework.permissions import IsAuthenticated


class TaskListAPIViewId(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')  # الحصول على user_id من بارامتر الاستعلام
        if not user_id:
            return Response({"detail": "user_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        # جلب المهام الخاصة بالمستخدم
        tasks = Task.collection.find({"user_id": user_id})  # البحث عن المهام باستخدام user_id
        
        task_data = []
        for task in tasks:
            task_data.append({
                'task_id': str(task['_id']),  # تحويل ObjectId إلى str
                'user_id': str(task['user_id']),  # تحويل ObjectId إلى str
                'title': task['title'],
                'description': task['description'],
                'start_date': task['start_date'],
                'end_date': task['end_date'],
                'repetition': task['repetition'],
                'status': task['status'],
            })
        
        return Response(task_data, status=status.HTTP_200_OK)

class TaskListAPIView(APIView):
    def get(self, request):
        # جلب جميع المهام من MongoDB باستخدام collection.find()
        tasks = Task.collection.find()  # جلب جميع المهام من collection
        
        # تحويل البيانات إلى قائمة بحيث يمكن إرسالها في الاستجابة
        task_data = []
        for task in tasks:
            task_data.append({
                'task_id': str(task['_id']),  # تحويل ObjectId إلى str
                'user_id': str(task['user_id']),  # تحويل ObjectId إلى str إذا لزم الأمر
                'title': task['title'],
                'description': task['description'],
                'start_date': task['start_date'],
                'end_date': task['end_date'],
                'repetition': task['repetition'],
                'status': task['status'],
            })
        
        return Response(task_data, status=status.HTTP_200_OK)

class TaskCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]  # التأكد من أن المستخدم مسجل دخوله

    def post(self, request):
        # الحصول على بيانات المهمة من الطلب
        task_data = request.data
        
        # إضافة معرّف المستخدم المسجل إلى بيانات المهمة
        task_data['user_id'] = str(request.user.id)  # استخدام معرف المستخدم المسجل حاليًا
        
        # استخدام الـ Serializer لتخزين البيانات
        serializer = TaskSerializer(data=task_data)
        
        if serializer.is_valid():
            task = serializer.save()  # حفظ المهمة مع بيانات المستخدم
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskListByDateAPIView(APIView):
    def get(self, request):
        # جلب المهام من MongoDB، مرتبة حسب start_date
        tasks = Task.collection.find().sort('start_date', 1)  # 1 لترتيب تصاعدي حسب start_date
        
        task_data = []
        for task in tasks:
            task_data.append({
                'task_id': str(task['_id']),  # تحويل ObjectId إلى str
                'user_id': str(task['user_id']),  # تحويل ObjectId إلى str
                'title': task['title'],
                'description': task['description'],
                'start_date': task['start_date'],
                'end_date': task['end_date'],
                'repetition': task['repetition'],
                'status': task['status'],
            })
        
        return Response(task_data, status=status.HTTP_200_OK)
