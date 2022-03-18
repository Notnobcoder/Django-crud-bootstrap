
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from registration.forms import RegistraionForm
from registration.models import Registraion_model

# Create your views here.
def index(request):
    if request.method=="POST":
        form=RegistraionForm(request.POST)
        if form.is_valid():
            form.save()
            form=RegistraionForm()
            messages.success(request,"registration completed")
    else:
        form=RegistraionForm()
    return render(request,"add.html",{"form":form})

def show(request):
    formdata=Registraion_model.objects.all()
    return render(request,"show.html",{"formdata":formdata})

def update(request,id):
    if request.method=="POST":
        ss=Registraion_model.objects.get(pk=id)
        fs=RegistraionForm(request.POST, instance=ss)
        if fs.is_valid():
            fs.save()
            fs=RegistraionForm()
    else:
        ss=Registraion_model.objects.get(pk=id)
        fs=RegistraionForm(instance=ss)
        
    return render(request,"update.html",{"form":fs})

def delete(request,id):
    ss=Registraion_model.objects.get(pk=id)
    ss.delete()
    return HttpResponseRedirect("/show/")