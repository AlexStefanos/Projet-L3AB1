from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.urls import router as transaction

router = routers.DefaultRouter()
# router.registry.extends(transaction.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('stats/',include('stats.urls')),
    path('api/',include(router.urls)),
    
]
