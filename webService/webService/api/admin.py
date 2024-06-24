from django.contrib import admin
from app.models import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'precio', 'cantidad', 'descripcion')
    list_editable = ('precio', 'cantidad', 'descripcion')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'direccion')
    list_editable = ('email', 'direccion')
    
class CatergoriaProductoAdmin(admin.ModelAdmin):
    list_display = ['categoria']


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente, ClienteAdmin)