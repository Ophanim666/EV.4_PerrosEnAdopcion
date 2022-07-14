from rest_framework import serializers
from .models import productos_a 

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = productos_a 
        fields = '__all__'



