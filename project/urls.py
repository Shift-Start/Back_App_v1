from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('login.urls')),
    path('account/', include('account.urls')),
    path('task/', include('task.urls')),
    path('habit/', include('habit.urls')),
    path('team/', include('team.urls')),
]

