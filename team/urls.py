from django.urls import path
from team.views import (
    TeamListCreateView,
    TeamMemberListCreateView,
    TeamUpdateView,
    TeamDeleteView,
    TeamMemberUpdateView,
    TeamMemberDeleteView,
)

urlpatterns = [
    path('teams/', TeamListCreateView.as_view(), name='team-list-create'),
    path('team-members/', TeamMemberListCreateView.as_view(), name='team-member-list-create'),
    path('teams/<str:team_id>/', TeamUpdateView.as_view(), name='team-update'),
    path('teams/<str:team_id>/delete/', TeamDeleteView.as_view(), name='team-delete'),
    path('team-members/<str:team_member_id>/', TeamMemberUpdateView.as_view(), name='team-member-update'),
    path('team-members/<str:team_member_id>/delete/', TeamMemberDeleteView.as_view(), name='team-member-delete'),
]


# {
#     "name": "Team Alpha",
#     "admin_id": "admin123",
#     "goal": "Complete the project",
#     "setting_team": {
#         "max_members": 10,
#         "privacy": "private"
#     }
# }


# POST /team-members/
# {
#     "team_id": "team123",
#     "user_id": "user456",
#     "permissions": {
#         "can_edit": true,
#         "can_delete": false
#     }
# }
