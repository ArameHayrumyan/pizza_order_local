from django.shortcuts import render, HttpResponse
from .models import Ingredients
# Create your views here.
def ingredients(request):
    return HttpResponse('Dougths, Cheeses, Sauces, Meat products, Spicery')

def ingredients_by_type(request, ingredient_type):
    try:
        ingredients = Ingredients.objects.filter(type=ingredient_type)
    except Ingredients.DoesNotExist:
        ingredients = None

    return render(request, 'ingridients_by_type.html', {'ingredients': ingredients, 'type': ingredient_type})