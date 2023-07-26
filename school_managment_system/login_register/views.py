from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from . import models
from .globalx import Globalx 

def login(request):
    if request.method=="GET":   
        return render(request, "login.html")
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            isUnique = models.UsersModel.objects.get(username=username)
            id = isUnique.pk
            if models.UsersModel.objects.get(pk=id).password==password:
                Globalx.isLoggedIn=True
                return HttpResponseRedirect(f"http://127.0.0.1:8000/tsi/{id}")
            else:
                return HttpResponse("password is incorrect")

        except:
            return HttpResponse("there is no username like that.")

def register(request):
    boolean = False
    if request.method=="GET":
        registerForm = models.UsersForm()
        return render(request, "register.html", {"registerForm":registerForm, "boolean":boolean})
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        role=request.POST["role"]
        form = models.UsersModel(username=username, password=password, role=role)
        if username!="" and password!="":
            form.save()
            return render(request, "successR.html")
        else:
            boolean=True
            registerForm = models.UsersForm()
        return render(request, "register.html", {"registerForm":registerForm, "boolean":boolean})
def logout(request):
    if Globalx.isLoggedIn:
        Globalx.isLoggedIn=False
        return HttpResponse("Logged out")
    else:
        return HttpResponse("You should first login")