from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cliente(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    direccion = models.CharField(max_length=200, null=False, blank=False)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "db_cliente"
   
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    marca = models.CharField(max_length=100,null=False)
    descripcion = models.CharField(max_length=500)
    create_at = models.DateTimeField(auto_now_add=True, null=False)
    update_at = models.DateTimeField(auto_now=True, null=False )

    class Meta:
        db_table = "Producto"

    def __str__(self):
        return self.nombre_producto
    

class Estado(models.Model):
    ESTADOS= [(1, 'Aceptado'), 
              (2, 'En proceso'), 
              (3, 'Enviado'),  
              (4, 'Finalizado'), 
              (5, 'Reembolsado'), 
              (6, 'Pendiente de pago')]
    id_estado = models.AutoField(choices=ESTADOS,primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre  
    
class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    subtotal = models.IntegerField(null=False)
    iva = models.IntegerField(null=False)
    total = models.IntegerField(null=False)
    fecha = models.DateField(null=False,auto_now_add=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = "pedido"

    def __str__(self):
        return self.cliente.nombre

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=False)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=False)
    cantidad = models.IntegerField()
    
    class Meta:
        unique_together = (('pedido', 'producto'),)

class MetodoPago(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000, null=True)
    
    def __str__(self):
        return self.nombre
    
class EstadoPago(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    
class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=False)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE, null=False)
    estado_pago = models.ForeignKey(EstadoPago, on_delete=models.CASCADE, null=False)
    monto = models.IntegerField()
    fecha = models.DateField()

class Transaccion(models.Model):
    id_transaccion = models.IntegerField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE, null=False)
    

class Carrito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    @property
    def get_cart_total(self):
        itemscarrito = self.itemcarrito_set.all()
        total = sum([item.get_total for item in itemscarrito])
        return total
    
    @property
    def get_cart_tipo(self):
        if self.itemcarrito_set.exists():
            primer_item = self.itemcarrito_set.first()  # Obtener el primer elemento del carrito
            tipo_producto = primer_item.producto.tipo # Obtener el nombre del tipo del objeto del primer elemento
            return tipo_producto
        else:
            return None 
        
    @property
    def get_cart_items(self):
        itemscarrito = self.itemcarrito_set.all()
        total = sum([item.cant for item in itemscarrito])
        return total

    class Meta:
        managed = True
        db_table = "db_carrito"


class ItemCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,null=False)
    pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE,null=False)
    cant = models.IntegerField(default=0)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE,null=False)

    def __str__(self):
        return self.producto.nom_producto
    
    @property
    def get_total(self):
        total = self.producto.precio * self.cant
        return total

    class Meta:
        db_table = "db_item_carrito"
