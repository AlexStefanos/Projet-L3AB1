from django.urls import path
from . import views

urlpatterns = [
    path('', views.adress_index, name ='adress_index'),
]
