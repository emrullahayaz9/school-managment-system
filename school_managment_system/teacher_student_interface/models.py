from django.db import models
from django.forms import ModelForm
from login_register.models import UsersModel


class Grades(models.Model):
    def __init__(self):
        UsersModel.objects.all().filter(role="S").values() # when new users added, this filter should call
    def caller():
        listx=[]
        user = list(UsersModel.objects.all().filter(role="S").values())
        for i in user:
            listx.append((i["username"], i["username"]))
        tuplex=tuple(listx)
        return tuplex

    lesson_code = models.CharField(max_length=100)
    student = models.CharField(max_length=100, choices=caller())
    grade = models.IntegerField()


class GradesForm(ModelForm):
    class Meta:
        model=Grades
        fields="__all__"

   


