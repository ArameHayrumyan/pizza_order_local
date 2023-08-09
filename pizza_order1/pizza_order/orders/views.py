from django.shortcuts import render, get_object_or_404, HttpResponse
from ingredients.models import Ingredients
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer, IngredientSerializer
from uuid import UUID

def pizza_builder(request):
    ingredients = Ingredients.objects.all()  # Получите все ингредиенты из базы данных
    return render(request, 'orders.html', {'ingredients': ingredients})




class CreateOrderView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            serializer = OrderSerializer(data=request.data)
            if serializer.is_valid():
                order = serializer.save()

                # Вычисление цены и времени на основе выбранных ингредиентов
                total_price = 0
                max_cooking_time = 0

                ingredient_ids = request.data['meat_products'] + request.data['cheese'] + request.data['spicery']
                
                dough = Ingredients.objects.get(pk=request.data['dough'])
                sauce = Ingredients.objects.get(pk=request.data['sauce'])
                meat_products = Ingredients.objects.filter(pk__in=ingredient_ids)

                ingredients = [dough, sauce] + list(meat_products)
                
                for ingredient in ingredients:
                    total_price += ingredient.price
                    if ingredient.time > max_cooking_time:
                        max_cooking_time = ingredient.time
                
                order.total_price = total_price
                order.max_cooking_time = max_cooking_time
                order.save()

                return Response({"message": "Order created successfully", "order_id": order.id}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
def order_detail_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)    
    # Вычисляем оставшееся время и цену
    remaining_time = order.remaining_time()
    total_price = order.total_price
    
    context = {
        'order': order,
        'remaining_time': remaining_time,
        'total_price': total_price,
    }
    
    return render(request, 'order_detail.html', context)

def confirm_order(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
        # Здесь можно добавить дополнительную логику, например, отправку подтверждения клиенту
        
        order.delete()  # Удаляем заказ из базы данных

    except Order.DoesNotExist:
        pass
    return HttpResponse("Your order was succsesfully confirmed!")
    