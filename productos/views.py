from django.http import HttpResponse, JsonResponse
from .models import Producto

#------------------------------------------------------------------------------------------

def inicio(request):
    return HttpResponse('Módulo de Productos Activo!')

#------------------------------------------------------------------------------------------

def acerca(request):
    return HttpResponse('API de ejemplo para la práctica (semana 3).')

#------------------------------------------------------------------------------------------

def api_productos2(request):
        productos = Producto.objects.all()
        datos = []
        for producto in productos:
            datos.append({
                 'id':producto.id,
                 'nombre':producto.nombre,
                 'descripcion':producto.descripcion,
                 'precio':float(producto.precio),
                 'stock':producto.stock,
                 'activo':producto.activo,
            })
        return JsonResponse({'productos':datos})

#------------------------------------------------------------------------------------------

def api_productos(request):
        productos = Producto.objects.values(
              'id', 'nombre', 'precio', 'stock'
        )
        
        return JsonResponse({'productos':list(productos)})

#------------------------------------------------------------------------------------------
