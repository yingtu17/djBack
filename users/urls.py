from django.urls import path

from . import views

urlpatterns = [
    path('', views.register, name='index'),
    path('lookUp',views.lookUp),
    path('register',views.register)
]