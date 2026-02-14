from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet
from .views import *

urlpatterns = [
    path('api/schema/',SpectacularAPIView.as_view(),name='schema'),
    path('api/docs/',SpectacularSwaggerView.as_view(url_name='schema')),
]


