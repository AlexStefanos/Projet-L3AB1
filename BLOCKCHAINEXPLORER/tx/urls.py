from django.urls import path
from . import views

urlpatterns = [
    path('', views.tx_index, name ='tx_index'),
]
