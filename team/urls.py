from django.urls import path
from team.views import (
    TeamListCreateView,
    TeamMemberListCreateView,
    TeamTasksByTeamView,
    TeamUpdateView,
    TeamDeleteView,
    TeamMemberUpdateView,
    TeamMemberDeleteView,
    TeamTaskListCreateView,
    TeamTaskUpdateView,
    TeamTaskDeleteView,
    MemberTaskListView,
)

urlpatterns = [
    path('teams/', TeamListCreateView.as_view(), name='team-list-create'),
    path('team-members/', TeamMemberListCreateView.as_view(), name='team-member-list-create'),
    path('teams/<str:team_id>/', TeamUpdateView.as_view(), name='team-update'),
    path('teams/<str:team_id>/delete/', TeamDeleteView.as_view(), name='team-delete'),
    path('team-members/<str:member_id>/', TeamMemberUpdateView.as_view(), name='team-member-update'),
    path('teams/<str:team_id>/tasks/', TeamTaskListCreateView.as_view(), name='team-task-list-create'),
    path('team-members/<str:member_id>/tasks/', MemberTaskListView.as_view(), name='member-task-list'),
    path('teams/<str:team_id>/tasks/<str:task_id>/', TeamTaskUpdateView.as_view(), name='team-task-update'),
    path('teams/<str:team_id>/tasks/<str:task_id>/delete/', TeamTaskDeleteView.as_view(), name='team-task-delete'),
    path('teams/<str:team_id>/tasks/', TeamTasksByTeamView.as_view(), name='team-tasks-by-team'),

]


# http://127.0.0.1:8000/team/teams/<team_id>/tasks/<task_id>/ تعديل مهمة معينة وفق id الفريق و id التاسك
# {
#   "team_id": "677d1392a0b32fe817f722a9",
#   "description": "Somen 789456",
#   "start_date": "2025-01-07T09:00:00",
#   "end_date": "2025-01-07T17:00:00",
#   "status": "In Progress",
#   "assigned_member_id":"677d185b476e52d157985e5a"
# }

# http://127.0.0.1:8000/team/teams/<team_id>/tasks/<task_id>/delete/ حذف مهمة معينة 
# http://127.0.0.1:8000/team/teams/tasks/ ظهور جميع الفرق
# http://127.0.0.1:8000/team/team-members/ ظهور جميع الاعضاء للفرق
# http://127.0.0.1:8000/team/team-members/<member_id>/tasks/  ظهور مهام عن طريق id العضو