from django.urls import path
from . import views

urlpatterns = [
    path('getExemple',views.getExemple),
    path('getInfoBlock/<int:pk>',views.getBlockInfo),
]