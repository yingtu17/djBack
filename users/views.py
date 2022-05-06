import json
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from users.models import Users


def register(request):
    name = request.POST.get('name')
    passw = request.POST.get('passw')
    passw_r = request.POST.get('passw_r')
    if passw != passw_r:
        return HttpResponse('Password not matched')
    client = Users(username=name,password = passw)
    client.save()
    return HttpResponse("Successfully registered.")

def lookUp(request):
    name =request.POST.get('')
    passw = request.POST.get('')
    try:
        client = Users.objects.get(username = name) 
    except:
        return HttpResponse('The user does not exists')
    if(client.password == passw):
        return HttpResponse("True.")

    return HttpResponse("Password is not correct")
