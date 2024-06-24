from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from app.models import *
from .serializers import *
    

class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        self.user = User.objects.create(**self.user_data)
        self.serializer = UserSerializer(instance=self.user)

    def test_serialization(self):
        data = self.serializer.data
        self.assertEqual(data['username'], self.user_data['username'])
        self.assertEqual(data['email'], self.user_data['email'])

    def test_deserialization(self):
        data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'newpassword'
        }
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        user = serializer.save()
        self.assertEqual(user.username, data['username'])
        self.assertEqual(user.email, data['email'])

class ProductoSerializerTestCase(TestCase):
    def setUp(self):
        self.producto_data = {
            'nombre_producto': 'Producto de prueba',
            'precio': 10990,
            'cantidad': 5,
            'marca':'taladrin',
            'descripcion':'taladro para taladrar'
        }
        self.producto = Producto.objects.create(**self.producto_data)
        self.serializer = ProductoSerializer(instance=self.producto)

    def test_serialization(self):
        data = self.serializer.data
        self.assertEqual(data['nombre_producto'], self.producto_data['nombre_producto'])
        self.assertEqual(data['precio'], self.producto_data['precio'])
        self.assertEqual(data['cantidad'], self.producto_data['cantidad'])
        self.assertEqual(data['marca'], self.producto_data['marca'])
        self.assertEqual(data['descripcion'], self.producto_data['descripcion'])

    def test_deserialization(self):
        data = {
            'nombre_producto': 'martillo',
            'precio': 16000,
            'cantidad': 5,
            'marca':'taladrin',
            'descripcion':'martillo martillin'
        }
        serializer = ProductoSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        producto = serializer.save()
        self.assertEqual(producto.nombre_producto, data['nombre_producto'])
        self.assertEqual(producto.precio, data['precio'])
        self.assertEqual(producto.cantidad, data['cantidad'])
        self.assertEqual(producto.marca, data['marca'])
        self.assertEqual(producto.descripcion, data['descripcion'])

class EstadoSerializerTestCase(TestCase):
    def setUp(self):
        self.estado_data = {
            'nombre': 'Estado de prueba',
        }
        self.estado = Estado.objects.create(**self.estado_data)
        self.serializer = EstadoSerializer(instance=self.estado)

    def test_serialization(self):
        data = self.serializer.data
        self.assertEqual(data['nombre'], self.estado_data['nombre'])

class PedidoSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com', password='testpassword')
        self.cliente_data = {
            'user': self.user,
            'nombre': 'Cliente de prueba',
            'email': 'tG3Rn@example.com',
            'direccion':'mi casa 1234'
        }
        self.cliente = Cliente.objects.create(**self.cliente_data)

        self.estado_data = {
            'nombre': 'Estado de prueba',
        }
        self.estado = Estado.objects.create(**self.estado_data)

        self.pedido_data = {
            'cliente': self.cliente,
            'estado': self.estado,
            'subtotal': 10990,
            'iva': 19,
            'total': 10990
        }
        self.pedido = Pedido.objects.create(**self.pedido_data)
        self.serializer = PedidoSerializer(instance=self.pedido)

    def test_serialization(self):
        data = self.serializer.data
        # Verifica que los datos serializados sean correctos
        self.assertEqual(data['cliente']['nombre'], self.cliente_data['nombre'])
        self.assertEqual(data['estado']['nombre'], self.estado_data['nombre'])

# class DetallePedidoSerializerTestCase(TestCase):
#     def setUp(self):
#         # Crea datos de ejemplo para el producto y el pedido
#         self.producto_data = {
#             'nombre_producto': 'Producto de prueba',
#             'precio': 10990,
#             'cantidad': 100,
#             'marca':'taladrin',
#             'descripcion':'taladro para taladrar'  
#         }
#         self.producto = Producto.objects.create(**self.producto_data)

#         self.user = User.objects.create(username='testuser', email='test@example.com', password='testpassword')
#         self.cliente_data = {
#             'user': self.user,
#             'nombre': 'Cliente de prueba',
#             'email': 'tG3Rn@example.com',
#             'direccion':'mi casa 1234'
#         }
#         self.cliente = Cliente.objects.create(**self.cliente_data)

#         self.estado = Estado.objects.create(nombre='validado')
#         self.pedido_data = {
#             'cliente':self.cliente,
#             'estado':self.estado,
#             'subtotal': 10000,
#             'iva': 19,
#             'total': 15000,
            
#         }
#         self.pedido = Pedido.objects.create(**self.pedido_data)

#         self.detalle_pedido_data = {
#             'pedido': self.pedido,
#             'producto': self.producto,
#             'cantidad': 5,  
#         }
#         self.serializer = DetallePedidoSerializer(instance=self.detalle_pedido_data)

#     def test_validation(self):
#         serializer = DetallePedidoSerializer(data=self.detalle_pedido_data)
#         self.assertTrue(serializer.is_valid())
#         data = self.serializer.validated_data
#         self.assertEqual(data['cantidad'], self.detalle_pedido_data['cantidad'])

#         # Prueba de validación de stock
#         detalle_pedido_data_modified = self.detalle_pedido_data.copy()  # Crear una copia del diccionario
#         detalle_pedido_data_modified['cantidad'] = 200  # Modificar la cantidad en la copia
#         with self.assertRaises(serializers.ValidationError):
#             serializer = DetallePedidoSerializer(data=detalle_pedido_data_modified)
#             serializer.is_valid(raise_exception=True)

#     def test_create(self):
#         serializer = DetallePedidoSerializer(data=self.detalle_pedido_data)
#         self.assertFalse(serializer.is_valid())  # Asegúrate de llamar a .is_valid() primero
#         detalle_pedido = serializer.save()  # Usa .save() en lugar de .create()
#         self.assertEqual(detalle_pedido.producto.stock, 95)  # Stock actualizado

#         # Prueba de cálculo de subtotal, iva y total en el pedido
#         self.assertEqual(self.pedido.subtotal, 54.95)  # Ajusta según tus datos
#         self.assertEqual(self.pedido.iva, 10.45)
#         self.assertEqual(self.pedido.total, 65.4)