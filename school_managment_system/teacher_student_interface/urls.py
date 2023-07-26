from django.urls import path
from . import views
urlpatterns = [
    path('<int:id>', views.redirection, name = "redirection"),
    path('teacher', views.teacher_interface, name = "teacher"),
    path('student/<str:username>', views.student_interface, name = "student"),
]
