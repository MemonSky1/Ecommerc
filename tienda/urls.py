from . import views
from django.urls import path, include

app_name = 'tienda'

urlpatterns = [
    
    path('', views.inicio, name='inicio'),
    path('productos/', views.productos, name='productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('ver-formularios/', views.ver_formularios, name='ver_formularios'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('aceptar/<int:pk>/', views.aceptar_producto, name='aceptar_producto'),
    path('eliminar_2/<int:pk>/', views.eliminar_producto_2, name='eliminar_producto_2'),
    path('agregar-al-carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('eliminar-del-carrito/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('comprar/', views.comprar, name='comprar'),
]
