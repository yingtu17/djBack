import json
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from users.models import Users
import json



def register(request):
    data = json.loads(request.body.decode('utf-8'))
    email = data['email']
    passw = data['password']
    passw_r = data['conpassword']
    if passw != passw_r:
        return HttpResponse('Password not matched')
    client = Users(username=email,password = passw)
    client.save()
    return HttpResponse("Successfully registered.")

def lookUp(request):
    name =request.POST.get('logemail')
    passw = request.POST.get('logpassword')
    try:
        client = Users.objects.get(username = name) 
    except:
        return HttpResponse('The user does not exists')
    if(client.password == passw):
        return HttpResponse("True.")

    return HttpResponse("Password is not correct")
