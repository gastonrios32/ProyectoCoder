from django.http.response import HttpResponse
from django.shortcuts import render


def inicio (request):
    return render(request,'AppCoder/inicio.html')

def cursos (request):
    return HttpResponse('vista cursos')

def profesores (request):
    return HttpResponse('vista profesores')

def estudiantes (request):
    return HttpResponse('vista estudiantes')

def entregables (request):
    return HttpResponse('vista entregables')