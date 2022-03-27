from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('stats/',include('stats.urls')),
    path('api/',include('api.urls')),
    path('documentation/', include('documentation.urls')),
]
