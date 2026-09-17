from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio_productos'),
    path('acerca/', views.acerca, name='acerca_productos'),

    # Productos.
    path('api/productos/', views.api_productos, name='api_productos'),

    path('api/productos/<int:pk>/', views.detalle_productos, name='detalle_producto'),

    # Categorías.
    path('api/categorias/', views.api_categorias, name='api_categorias'),

    path('api/categorias/resumen/', views.resumen_categorias, name='resumen_categorias'),

    path('api/categorias/<int:pk>/', views.detalle_categorias, name='detalle_categoria'),

    # Seguridad.
    path('api/perfil/', views.perfil, name='api_perfil'),
    path('api/admin-info/', views.panel_admin_api, name='panel_admin_info'),

    # Sesión.
    path('api/sesion/', views.contador_sesion, name='contador_sesion'),
]
