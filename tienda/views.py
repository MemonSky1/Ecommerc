from .models import Producto, default_username
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render,redirect,get_object_or_404
from .forms import ProductoForm
from django.contrib.admin.views.decorators import staff_member_required
from .models import Carrito
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, 'tienda/inicio.html')



def productos(request):
    productos_aprobados = Producto.objects.filter(aprobado=True)
    return render(request, 'tienda/productos.html', {'productos': productos_aprobados})


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user
            producto.save()
            return redirect('tienda:inicio') 
    else:
        form = ProductoForm()
    return render(request, 'tienda/agregar_producto.html', {'form': form})

@staff_member_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('tienda:ver_formularios')

@staff_member_required
def eliminar_producto_2(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('tienda:productos')

@staff_member_required
def ver_formularios(request):
    productos_pendientes = Producto.objects.filter(aprobado=False)
    return render(request, 'tienda/ver_formularios.html', {'productos': productos_pendientes})

@staff_member_required
def aceptar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.aprobado = True
    producto.save()
    return redirect('tienda:ver_formularios')

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    if producto not in carrito.productos.all():
        carrito.productos.add(producto)
    return redirect('tienda:productos')

def ver_carrito(request):
    try:
        carrito = Carrito.objects.get(usuario=request.user)
        productos_en_carrito = carrito.productos.all()
        total = sum(producto.precio for producto in productos_en_carrito)
    except Carrito.DoesNotExist:
        return render(request, 'tienda/carrito_vacio.html')

    context = {
        'carrito': carrito,
        'productos': productos_en_carrito,
        'total': total,
    }
    return render(request, 'tienda/carrito.html', context)

def eliminar_del_carrito(request, producto_id):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    producto = get_object_or_404(Producto, pk=producto_id)
    carrito.productos.remove(producto)
    
    return redirect('tienda:inicio')

def comprar(request):
    if request.method == 'POST':
        try:
            carrito = Carrito.objects.get(usuario=request.user)
            productos_en_carrito = carrito.productos.all()
            for producto in productos_en_carrito:
                producto.aprobado = True
                producto.vendido = True
                producto.save()
            carrito.productos.clear()
        except Carrito.DoesNotExist:
            pass
    return redirect('tienda:inicio')