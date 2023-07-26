
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homePage.urls')),
    path('auth/', include('login_register.urls')),
    path('tsi/', include('teacher_student_interface.urls')),
]
