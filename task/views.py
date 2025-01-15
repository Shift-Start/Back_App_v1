from datetime import datetime
from string import Template
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bson import ObjectId
from rest_framework.permissions import AllowAny
from .serializers import TaskSerializer, TemplateSerializer
from .models import Task, TemplateModel
from django.views.decorators.csrf import csrf_exempt

def convert_object_id_to_string(task):
    task['_id'] = str(task['_id'])
    return task

class TaskListCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        try:
            data['Date'] = datetime.combine(datetime.strptime(data['Date'], '%Y-%m-%d'), datetime.min.time())
            data['StartDate'] = datetime.fromisoformat(data['StartDate'])
            data['EndDate'] = datetime.fromisoformat(data['EndDate'])
        except (ValueError, KeyError) as e:
            return Response({"error": "Invalid date format. Use 'YYYY-MM-DDTHH:MM:SS'."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = TaskSerializer(data=data)

        if serializer.is_valid():
            task_data = serializer.validated_data
            task_data['created_at'] = datetime.utcnow()
            task_data['updated_at'] = datetime.utcnow()
            
            created_task = Task.collection.insert_one(task_data)
            task_data['_id'] = str(created_task.inserted_id)
            return Response(task_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        tasks = list(Task.collection.find())
        task_list = [convert_object_id_to_string(task) for task in tasks]
        return Response(task_list, status=status.HTTP_200_OK)

#         استرجاع مهمة معينة باستخدام معرف المهمة.
class TaskDetailView(APIView):
    def get(self, request, task_id):
        try:
            task = Task.get_task_by_id(task_id)
            if task:
                return Response(task, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# استرجاع جميع المهام الخاصة بمستخدم معين
class UserTasksView(APIView):
    def get(self, request, user_id):
        tasks, status_code = Task.get_tasks_by_user_id(user_id)
        if status_code == 200:
            return Response(tasks, status=status.HTTP_200_OK)
        return Response(tasks, status=status.HTTP_404_NOT_FOUND if status_code == 404 else status.HTTP_500_INTERNAL_SERVER_ERROR)

# حذف التاسك
class TaskDeleteView(APIView):
    def delete(self, request, task_id):
        if not ObjectId.is_valid(task_id):
            return Response({"error": "Invalid Task ID"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            result, http_status = Task.delete_task(task_id)
            return Response(result, status=http_status)
        except Exception as e:
            return Response({"error": f"Unexpected error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# تعديل التاسك
class UpdateTaskView(APIView):
    def put(self, request, task_id):
        try:
            task_data = request.data
            result, code = Task.update_task(task_id, task_data)
            return Response(result, status=code)
        except ValueError as ve:
            return Response({"error": str(ve)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": f"Unexpected error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# استدعاء الدالة لاسترجاع جميع المهام
class GetAllTasksView(APIView):
    def get(self, request):
        try:
            tasks = Task.get_all_tasks()
            return Response({"tasks": tasks}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"Unexpected error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

          #عرض القوالب وإضافتها
class TemplateView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        templates = TemplateModel.get_all_templates()
        serializer = TemplateSerializer(templates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = TemplateSerializer(data=request.data)
        if serializer.is_valid():
            template = TemplateModel.insert_template(
                name=serializer.validated_data['name'],
                description=serializer.validated_data['description']
            )
            return Response(template, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteTemplateByNameView(APIView):
    @csrf_exempt  # تعطيل التحقق من CSRF لهذا الـ view
    def delete(self, request, template_name):
        try:
            result = TemplateModel.collection.delete_one({"name": template_name})
            if result.deleted_count > 0:
                return JsonResponse({"message": f"Template '{template_name}' deleted successfully."}, status=200)
            else:
                return JsonResponse({"error": f"No template found with name '{template_name}'."}, status=404)
        except Exception as e:
            return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)

class DeleteTemplateByIdView(APIView):
    @csrf_exempt  # تعطيل التحقق من CSRF لهذا الـ view
    def delete(self, request, template_id):
        try:
            if not ObjectId.is_valid(template_id):
                return JsonResponse({"error": "Invalid Template ID"}, status=400)
            result = TemplateModel.collection.delete_one({"_id": ObjectId(template_id)})
            if result.deleted_count > 0:
                return JsonResponse({"message": f"Template with ID '{template_id}' deleted successfully."}, status=200)
            else:
                return JsonResponse({"error": f"No template found with ID '{template_id}'."}, status=404)
        except Exception as e:
            return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)