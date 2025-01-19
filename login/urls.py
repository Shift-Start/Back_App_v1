from django.urls import path
from login.views import LoginAPIView,RegisterAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),
]


<<<<<<< HEAD

=======
>>>>>>> f70151a67db44782b0182c41b22e35dbcd1ed815
# {
#     "username": "new_user",
#     "email": "newuser@example.com",
#     "password": "securepassword123",
#     "is_admin": false

# }
# {
#     "email": "newuser@example.com",
#     "password": "securepassword123"
# }

# {
#     "username": "new_user123",
#     "email": "newuser123@example.com",
#     "password": "new_user123",
# }