from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio_productos'),
    path('acerca/', views.acerca, name='acerca_productos'),

    path('api/productos/', views.api_productos, name='api_productos'),

    path('api/productos/<int:pk>/', views.detalle_productos, name='detalle_producto')
]
