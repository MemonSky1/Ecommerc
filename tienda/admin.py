from django.contrib import admin

from .models import Carrito, Producto

admin.site.register(Producto)
admin.site.register(Carrito)