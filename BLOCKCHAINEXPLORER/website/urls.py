from django.urls import path
from . import views

urlpatterns = [
    path('', views.website_index, name ='website_index'),
    path('article/<str:name>/', views.article, name ='article'),

]
