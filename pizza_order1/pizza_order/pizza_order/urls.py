"""
URL configuration for pizza_order project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ingredients.views import ingredients
from ingredients.views import ingredients_by_type
from orders.views import pizza_builder, CreateOrderView, order_detail_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ingredients/', ingredients),
    path('ingredients/<str:ingredient_type>/', ingredients_by_type, name='ingredients_by_type'),
    path('pizza-builder/', pizza_builder, name='pizza-builder'),
    path('create-order/', CreateOrderView.as_view(), name='create-order'),
    path('order/<int:order_id>/', order_detail_view, name='order-detail')
]
