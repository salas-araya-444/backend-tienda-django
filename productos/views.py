from django.http import HttpResponse, JsonResponse
from .models import Producto, Categoria

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductoSerializer, CategoriaSerializer

#------------------------------------------------------------------------------------------

# API Productos.
@api_view(['GET', 'POST'])
def api_productos(request):
    if request.method == 'GET':
        productos = Producto.objects.all().order_by('id')
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

#------------------------------------------------------------------------------------------

# Detalle Productos.
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def detalle_productos(request, pk):
    try:
        producto = Producto.objects.get(pk=pk)
    except Producto.DoesNoExist:
        return Response(
            {'error':'Producto no encontrado...'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

    if request.method in ['PUT', 'PATCH']:
        serializer = ProductoSerializer(
            producto,
            data=request.data,
            partial=(request.method=='PATCH')
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    if request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#------------------------------------------------------------------------------------------

# API Categorías.
@api_view(['GET', 'POST'])
def api_categorias(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all().order_by('id')
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CategoriaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

#------------------------------------------------------------------------------------------

# Detalle Categorías.
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def detalle_categorias(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk)
    except Categoria.DoesNotExist:
        return Response(
            {'error': 'Categoría no encontrada...'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    if request.method in ['PUT', 'PATCH']:
        serializer = CategoriaSerializer(
            categoria,
            data=request.data,
            partial=(request.method == 'PATCH')
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    if request.method == 'DELETE':
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#------------------------------------------------------------------------------------------

# Resuemen Categorías (activas e inactivas).
@api_view(['GET'])
def resumen_categorias(request):
    total = Categoria.objects.count()

    activas = Categoria.objects.filter(activo=True).count()
    inactivas = Categoria.objects.filter(activo=False).count()

    return Response({
        'total': total,
        'activas': activas,
        'inactivas': inactivas
    })

#------------------------------------------------------------------------------------------

def inicio(request):
    return HttpResponse('Módulo de Productos Activo!')

#------------------------------------------------------------------------------------------

def acerca(request):
    return HttpResponse('API de ejemplo para la práctica (semana 3).')

#------------------------------------------------------------------------------------------

# def api_productos2(request):
#         productos = Producto.objects.all()
#         datos = []
#         for producto in productos:
#             datos.append({
#                  'id':producto.id,
#                  'nombre':producto.nombre,
#                  'descripcion':producto.descripcion,
#                  'precio':float(producto.precio),
#                  'stock':producto.stock,
#                  'activo':producto.activo,
#             })
#         return JsonResponse({'productos':datos})

#------------------------------------------------------------------------------------------

# def api_productos(request):
#         productos = Producto.objects.values(
#               'id', 'nombre', 'precio', 'stock'
#         )
        
#         return JsonResponse({'productos':list(productos)})

#------------------------------------------------------------------------------------------
