from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Services
from polls.models import User
from polls.models import UserService


def hello(request):
    return render(request, 'index.html', { 'data' : {
        'current_date': date.today(),
        'list': ['обследование', 'анализы', 'стационар']
    }})


def GetServices(request):
    return render(request, 'services.html', {'data' : {
        'current_date': date.today(),
        'services': Services.objects.all()
    }})


def GetService(request, id):
    return render(request, 'service.html', {'data' : {
        'current_date': date.today(),
        'service': Services.objects.filter(idservice=id)[0]
    }})


def GetUsers(request):
    return render(request, 'users.html', {'data' : {
        'current_date': date.today(),
        'users': User.objects.all()
    }})


def GetUser(request, id):
    return render(request, 'user.html', {'data' : {
        'current_date': date.today(),
        'users': User.objects.filter(iduser=id)[0],
        'services': Services.objects.all(),
        'user_services': UserService.objects.filter(id_user=id)
    }})
