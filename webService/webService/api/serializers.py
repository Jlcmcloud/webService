from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from app.models import *

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email','password')
    


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    
    def validate_username(self, value):
        if ' ' in value:
            raise serializers.ValidationError("Username should not contain spaces.")
        if len(value) < 5:  # Supongamos que la longitud mínima del username es 5
            raise serializers.ValidationError("Username is too short.")
        return value

    def validate_email(self, value):
        value = value.strip()
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def validate_password(self, value):
        if len(value.strip()) < 8:  # Supongamos que la longitud mínima de la contraseña es 8
            raise serializers.ValidationError("Password is too short.")
        return value


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__' 

class EstadoSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required=True)
    class Meta:
        model = Estado
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    estado = EstadoSerializer()
    class Meta:
        model = Pedido
        fields = '__all__'

class DetallePedidoSerializer(serializers.ModelSerializer):
    cantidad = serializers.IntegerField(required=True)
    
    class Meta:
        model = DetallePedido
        fields = ['pedido', 'producto', 'cantidad']
        
    def validate(self, data):
        producto = data['producto']
        cantidad = data['cantidad']

        if producto.stock < cantidad:
            raise serializers.ValidationError({'message': 'Producto agotado'})

        return data
        
    def create(self, validated_data):
        producto = validated_data['producto']
        cantidad = validated_data['cantidad']
        
        producto.stock -= cantidad
        producto.save()

        detalle_pedido = DetallePedido.objects.create(**validated_data)

        # Recuperar el pedido asociado
        pedido = detalle_pedido.pedido

        # Calcular el subtotal, iva y total
        subtotal = sum(detalle.producto.precio_neto * detalle.cantidad for detalle in DetallePedido.objects.filter(pedido=pedido))
        iva = subtotal * 0.19
        total = subtotal + iva

        # Guardar los valores calculados en el pedido
        pedido.subtotal = subtotal
        pedido.iva = iva
        pedido.total = total
        pedido.save()

        return detalle_pedido


#Metodo pago
class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = ['nombre']

class MetodoPagoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = ['nombre']


#Estado pago en el pedido
class EstadoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoPago
        fields = ['nombre']
    
class EstadoPagoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoPago
        fields = ['nombre']



class PagoSerializer(serializers.ModelSerializer):
    pedido = PedidoSerializer()
    metodo_pago = MetodoPagoSerializer()
    estado_pago = EstadoPagoSerializer()
    
    class Meta:
        model = Pago
        fields = ['pedido', 'metodo_pago', 'estado_pago', 'monto', 'fecha']

class PagoPostSerializer(serializers.ModelSerializer):
    fecha = serializers.DateField(required=True)

    class Meta:
        model = Pago
        fields = ['pedido', 'metodo_pago', 'estado_pago','monto', 'fecha']


class TransaccionSerializer(serializers.ModelSerializer):
    pedido = PedidoSerializer()
    cliente = Cliente()
    pago = PagoSerializer()
    
    class Meta:
        model = Transaccion
        fields = ['pedido', 'cliente', 'pago']


        
class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = '__all__'

class ItemCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCarrito
        fields = '__all__'

class ProductoPostSerializer(serializers.ModelSerializer):
    nombre_producto = serializers.CharField(required=True)
    precio = serializers.CharField(required=True)
    cantidad = serializers.CharField(required=True)
    marca = serializers.CharField(required=True)
    
    def validate(self, data):
        cantidad = data['stock']
        if cantidad < 0:
            raise serializers.ValidationError({'message': 'Cantidad no valida'})
        return data
    
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'precio', 'cantidad', 'marca']


