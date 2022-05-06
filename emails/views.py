from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail



# Create your views here.
def send(request):
    mail = request.POST.get('email')
    client_name = request.POST.get('name')
    msg = request.POST.get('message')
    send_mail(
        'Subject',
        'Here is the message from '+str(mail)+'\nname: '+str(client_name)+' \nmessage: '+str(msg),
        settings.EMAIL_HOST_USER,
        ['m473983663@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse('Email sent.')