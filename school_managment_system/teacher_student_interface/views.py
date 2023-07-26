from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from login_register.models import UsersModel
from .models import Grades, GradesForm
def redirection(request, id):
    userRole = UsersModel.objects.get(pk=id).role
    if userRole=="T":
        return HttpResponseRedirect("http://127.0.0.1:8000/tsi/teacher")
    if userRole=="S":
        return HttpResponseRedirect(f"http://127.0.0.1:8000/tsi/student/{UsersModel.objects.get(pk=id).username}")
    
def teacher_interface(request):
    form = GradesForm()
    boolean =False
    if request.method=="GET":
        return render(request, "teacher_interface.html", {"form":form})
    
    if request.method=="POST":
        bool2=False
        lesson_code = request.POST["lesson_code"]
        student = request.POST["student"]
        grade = request.POST["grade"]
        if lesson_code!="" and grade!="" and student!="":
            Grades(lesson_code=lesson_code, student=student, grade=grade).save()
            bool2=True
            success="successfuly registered"
            return render(request, "teacher_interface.html", {"success":success, "bool2":bool2, "form":form})

        else:
            boolean = True
            error_message = "form is not valid" 
            return render(request, "teacher_interface.html", {"error_message":error_message, "boolean":boolean, "form":form})
def student_interface(request, username):
    bool3=False
    try:
        info = Grades.objects.get(student=username)
        bool3=True
        return render(request, "student_interface.html", {"info":info,"bool3":bool3})
    except: 
        error_message = "Not yet"
        return render(request, "student_interface.html", {"error_message":error_message,"bool3":bool3})
