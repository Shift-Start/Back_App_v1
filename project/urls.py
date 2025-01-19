from django.contrib import admin
from django.urls import path,include

urlpatterns = [
<<<<<<< HEAD
    path('admin/', admin.site.urls),
    path('user/', include('login.urls')),
    path('account/', include('account.urls')),
    path('task/', include('task.urls')),
    path('habit/', include('habit.urls')),
    path('team/', include('team.urls')),
=======
        path('admin/', admin.site.urls),
    path('api/login/', include('login.urls')),
    path('api/tasks/', include('task.urls')),  # تأكد من ربط tasks هنا
>>>>>>> f70151a67db44782b0182c41b22e35dbcd1ed815
]

