from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User

def default_username():
    try:
        user = User.objects.get(username='Demian')
        return user.id
    except User.DoesNotExist:
        return None

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    aprobado = models.BooleanField(default=False)
    vendido = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.titulo
    
class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)

    def __str__(self):
        return f'Carrito de {self.usuario.username}'