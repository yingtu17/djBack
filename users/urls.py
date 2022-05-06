from django.urls import path

from . import views

urlpatterns = [
    path('', views.register, name='index'),
    path('login',views.lookUp),
    path('register',views.register)
]