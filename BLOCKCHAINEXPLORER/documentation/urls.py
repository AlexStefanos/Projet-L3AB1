from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index_documentation.html',extra_context={'schema_url':'api_schema'}), name='swagger-ui'),
]
