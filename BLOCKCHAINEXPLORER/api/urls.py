from django.urls import path
from . import views

urlpatterns = [
    path('getLastBlock',views.getLastBlock),
    path('getInfoBlock/<int:pk>',views.getBlockInfo),
    path('getInfoHashBlock/<int:pk>',views.getInfoHashBlock),
    path('getFromTo/<str:pk>',views.getFromTo),
    path('getWallet/<str:pk>',views.getWallet),
    path('getEthPrice',views.getEthPrice),
]