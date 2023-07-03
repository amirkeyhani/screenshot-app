from django.urls import path

from . import views

urlpatterns = [
    path('', views.screenshot, name='index'), 
]
