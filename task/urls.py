from django.urls import path
from task.views import (
    TaskDetailView,
    TaskListCreateView,
    UserTasksView,
    TaskDeleteView,
    UpdateTaskView,
    GetAllTasksView
)

urlpatterns = [
    # إنشاء وعرض المهام
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    # استرجاع مهمة معينة عن طريق TaskID
    path('tasks/<str:task_id>/', TaskDetailView.as_view(), name='task-detail'),
    # استرجاع جميع المهام الخاصة بمستخدم معين
    path('tasks/user/<str:user_id>/', UserTasksView.as_view(), name='user-tasks'),
    # حذف المهمة عن طريق id المهمة
    path('tasks/delete/<str:task_id>/', TaskDeleteView.as_view(), name='delete_task'),
    # تعديل على مهمة عم طريق id التاسك
    path('tasks/update/<str:task_id>/', UpdateTaskView.as_view(), name='update_task'),
    # استرجاع كافة المهام في قاعدة البيانات
    path('tasks/', GetAllTasksView.as_view(), name='get_all_tasks'),


]



#  إضافة مهمة جديدة           http://127.0.0.1:8000/api/tasks/tasks/
# {
#   "UserID": "user123",
#   "Title": "Complete Homework",
#   "Description": "Finish math homework before evening",
#   "Date": "2025-01-15", 
#   "StartDate": "2025-01-15T09:00:00",
#   "EndDate": "2025-01-15T12:00:00",
#   "repetition": "None",
#   "Status": "Pending"
# }

# http://127.0.0.1:8000/api/tasks/tasks/67869f5351973cc0e6d796a7/ استرجاع مهمة ما عن طريق id المهمة
# http://localhost:8000/api/tasks/tasks/user/64ae23f5cd6d4a1234567890/  استرجاع مهمة ما عن طريق id المستخدم
# http://127.0.0.1:8000/api/tasks/tasks/delete/6786a881ef3345ac72d5a201/ حذف مهمة عن طريق id المهمة
# http://127.0.0.1:8000/api/tasks/tasks/update/6787db08e744c291dc9b199b/ التعديل على مهمة عن طريق id المهمة
# http://127.0.0.1:8000/api/tasks/tasks/ استرجاع جميع المهام من قاعدة البيانات
