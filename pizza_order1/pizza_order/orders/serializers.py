from rest_framework import serializers
from .models import Order
from ingredients.models import Ingredients

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    remaining_time = serializers.ReadOnlyField()  # Добавляем поле для оставшегося времени
    total_price = serializers.ReadOnlyField() 
    class Meta:
        model = Order
        fields = '__all__'

