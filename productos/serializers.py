from rest_framework import serializers
from .models import Producto, Categoria

#------------------------------------------------------------------------------------------

# modelo = Producto: Indica que se transformara y validara.
# fields = '__all__': Expone todos los campos del modelo.

# Producto.
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

#------------------------------------------------------------------------------------------

    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                'El precio debe ser mayor a 0...'
            )
        return value

#------------------------------------------------------------------------------------------

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError(
                'El stock no puede ser negativo...'
            )
        return value

#------------------------------------------------------------------------------------------

# Categoria.
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

#------------------------------------------------------------------------------------------

    def validate_nombre(self, value):

        nombre_limpio = value.strip()

        if nombre_limpio == "":
            raise serializers.ValidationError(
                'El nombre no puede estar vacío...'
            )

        if len(nombre_limpio) < 3:
            raise serializers.ValidationError(
                'El nombre debe tener al menos 3 caracteres...'
            )
        return nombre_limpio

#------------------------------------------------------------------------------------------
