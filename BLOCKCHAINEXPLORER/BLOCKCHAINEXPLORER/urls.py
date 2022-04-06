from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView


urlpatterns = [
   path('api_schema/', get_schema_view(title='API Blockchain Explorer',description='Guide for the REST API of our university project'), name='api_schema'),
   path('docs/', include('documentation.urls')),
   path('admin/', admin.site.urls),
   path('',include('home.urls')),
   path('stats/',include('stats.urls')),
   path('api/',include('api.urls')),
   path('documentation/', include('documentation.urls')),
   path('tx/<str:pk>', include('tx.urls')),
   path('adress/<str:pk>', include('adress.urls')),
   #path('adress/', include('adress.urls')),

]
