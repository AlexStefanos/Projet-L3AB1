from django.urls import path
from . import views

urlpatterns = [
    path('getExemple',views.getExemple),
    path('getInfoBlock/<int:pk>',views.getBlockInfo),
    path('getFromTo/<str:pk>',views.getFromTo),
    path('getWallet/<str:pk>',views.getWallet),
    path('getEthPrice',views.getEthPrice),
]