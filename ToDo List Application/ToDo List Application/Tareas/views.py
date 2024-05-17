from django.shortcuts import render, redirect
from .models import Adminis

# Create your views here.



def home(request):
    Administ = Adminis.objects.all()
    return render(request, "Interfaz.html", {"Tareas": Administ})

def registarTarea(request):
    title=request.POST['txtTitle']
    descrip = request.POST['txtDescrip']
    
    tarea= Adminis.objects.create(Title=title, Descrip=descrip)
    return redirect('/')   
def actualizarTarea(request, Title):
    tarea=Adminis.objects.get(Title=Title)
    
    return render(request, "actualizarTarea.html", {"Tareas": tarea})


def ActualizarTarea(request):
    title=request.POST['txtTitle']
    descrip = request.POST['txtDescrip']
    
    tarea=Adminis.objects.get(Title=title)
    
    tarea.Title=title
    tarea.Descrip=descrip
    tarea.save()
    return redirect('/')   
def leerTarea(request, Title):
    tarea=Adminis.objects.get(Title=Title)
    
    return render(request, "Leer.html", {"Tareas": tarea})

def LeerTarea(request):
    title=request.POST['txtTitle']
    descrip = request.POST['txtDescrip']
    
    return redirect('/')
    
def eliminarTarea(request, Title):
    tarea=Adminis.objects.get(Title=Title)
    tarea.delete()
    return redirect('/')

