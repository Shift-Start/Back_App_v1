from django.urls import path
from task.views import TaskCreateAPIView, TaskListAPIView,TaskListAPIViewId,TaskListByDateAPIView
urlpatterns = [

    path('tasks/list/', TaskListAPIView.as_view(), name='task-list'),
    path('tasks/listId/', TaskListAPIViewId.as_view(), name='task-list-id'),
    path('tasks/create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('tasks/', TaskListByDateAPIView.as_view(), name='task-list-by-date'),
 ]




# {
#   "user_id": "ObjectId('67487642e70161b8d3c73ff0')",
#   "title": "Task Title",
#   "description": "Description of the task",
#   "start_date": "2024-12-01T10:00:00Z",
#   "end_date": "2024-12-01T12:00:00Z",
#   "repetition": "daily",
#   "status": "pending"
# }


# {
#   "user_id": "67487642e70161b8d3c73ff0",  // استبدل بقيمة user_id الفعلية
#   "title": "Task Title",                // العنوان الفعلي للمهمة
#   "description": "Description of the task",  // الوصف الفعلي للمهمة
#   "start_date": "2024-12-01T10:00:00Z",   // تاريخ بداية المهمة بتنسيق UTC
#   "end_date": "2024-12-01T12:00:00Z",     // تاريخ نهاية المهمة بتنسيق UTC
#   "repetition": "daily",                 // تكرار المهمة مثل "daily" أو "weekly" حسب الحاجة
#   "status": "pending"                    // حالة المهمة مثل "pending" أو "completed"
# }
# {
#   "user_id": "67487642e70161b8d3c73ff0", 
#   "title": "Task Title",              
#   "description": "Description of the task", 
#   "start_date": "2024-12-01T10:00:00Z",  
#   "end_date": "2024-12-01T12:00:00Z",     
#   "repetition": "daily",                
#   "status": "pending"                   
# }

