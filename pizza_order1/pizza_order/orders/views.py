from django.shortcuts import render, HttpResponse

# Create your views here.

def orders(request):
    return HttpResponse('orders.Home')