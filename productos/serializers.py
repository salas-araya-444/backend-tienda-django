from rest_framework import serializers
from .models import Producto

#------------------------------------------------------------------------------------------

# modelo = Producto: Indica que se transformara y validara.
# fields = '__all__': Expone todos los campos del modelo.
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
                'El precio no puede ser negativo...'
            )
        return value

#------------------------------------------------------------------------------------------
