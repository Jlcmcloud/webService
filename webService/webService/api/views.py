import datetime
import random
import requests
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.generics import *
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login
from base64 import b64decode
from app.models import *
from .serializers import *
from app.forms import *

# Create your views here.

class ObtainTokenView(APIView):
    def get(self, request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return Response({'error': 'Falta el encabezado de autorización'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            auth_type, auth_string = auth_header.split(' ')
            username, password = b64decode(auth_string).decode('utf-8').split(':')
        except ValueError:
            return Response({'error': 'Encabezado de autorización inválido'},
                            status=status.HTTP_401_UNAUTHORIZED)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Credenciales inválidas'},
                            status=status.HTTP_403_FORBIDDEN)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},
                        status=status.HTTP_200_OK)

#auth
@api_view(['POST'])
def login(request):

    user = get_object_or_404(User, username=request.data['username'])
    ##cambiar forma de obtener username y password
    #ingresar credenciales mediante auth
    if not user.check_password(request.data['password']):
        return Response({"error":"password incorrecta"},status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)

    serializer = UserSerializer(instance=user)

    return Response({"token": token.key,'user': serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    
    if request.method == 'POST':
        form = RegisterForm(data=request.data)
        if serializer.is_valid():  # Verifica si el serializador es válido
            user = serializer.save()  # Guarda el usuario creado

            if 'password' in serializer.data:
                user.set_password(serializer.data['password'])
                user.save()

            cli, create = Cliente.objects.get_or_create(user=user, nombre=user.get_username)
            cli.email = serializer.data['email']
            cli.save()

            token = Token.objects.create(user=user)

            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def perfil(request):

    print(request.user)

    return Response({"Estas logeado como {}".format(request.user.username)},status=status.HTTP_200_OK)

#api productos
        


# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])        # Obtenemos el valor de la URL utilizando 'self.kwargs'
class ProductoList(ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_object(self):
        # Obtenemos el valor de la URL utilizando 'self.kwargs'
        id = self.kwargs['id']
        # Usamos el filtro para encontrar el perfil correspondiente
        return Producto.objects.get(id=id)
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])         
class ProductoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_object(self):
        # Obtenemos el valor de la URL utilizando 'self.kwargs'
        id = self.kwargs['id']
        # Usamos el filtro para encontrar el perfil correspondiente
        return Producto.objects.get(id=id)
    
   
class ClienteList(ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get_object(self):
        # Obtenemos el valor de la URL utilizando 'self.kwargs'
        id = self.kwargs['id']
        # Usamos el filtro para encontrar el perfil correspondiente
        return Cliente.objects.get(id=id)

    
class ClienteDetalle(RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get_object(self):
        # Obtenemos el valor de la URL utilizando 'self.kwargs'
        id = self.kwargs['id']
        # Usamos el filtro para encontrar el perfil correspondiente
        return Cliente.objects.get(id=id)
"""
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
"""


"""
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
"""     
class CarritoList(ListCreateAPIView):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

    def create(self, request, *args, **kwargs):
        # Obtenemos el cliente del request
        cliente = request.data.get('cliente')

        # Verificamos si ya existe un carrito para ese cliente
        if Carrito.objects.filter(cliente=cliente).exists():
            return Response({"detail": "Ya existe un carrito para este cliente."}, status=status.HTTP_400_BAD_REQUEST)

        # Si no existe, delegamos la creación del carrito al comportamiento por defecto
        return super().create(request, *args, **kwargs)

    def get_object(self):
        # Obtenemos el valor de la URL utilizando 'self.kwargs'
        id = self.kwargs['id']
        # Usamos el filtro para encontrar el perfil correspondiente
        return Carrito.objects.get(id=id)
    
    
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])     
class CarritoDetalle(RetrieveUpdateDestroyAPIView):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

    def get_object(self):
        # Obtenemos el valor de la URL utilizando 'self.kwargs'
        id = self.kwargs['id']
        # Usamos el filtro para encontrar el perfil correspondiente
        return Carrito.objects.get(id=id)
""" 
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
"""     
class ItemCarritoList(ListCreateAPIView):
    queryset = ItemCarrito.objects.all()
    serializer_class = ItemCarritoSerializer

    def create(self, request, *args, **kwargs):
        # Obtenemos el cliente del request
        carrito = request.data.get('carrito')

        # Verificamos si ya existe un carrito para ese cliente
        if ItemCarrito.objects.filter(carrito=carrito).exists():
            return Response({"detail": "Ya existe un itemCarrito para est carro de compras."}, status=status.HTTP_400_BAD_REQUEST)

        # Si no existe, delegamos la creación del carrito al comportamiento por defecto
        return super().create(request, *args, **kwargs)

    def get_object(self):
        # Obtenemos el valor de la URL utilizando 'self.kwargs'
        id = self.kwargs['id']
        # Usamos el filtro para encontrar el perfil correspondiente
        return ItemCarrito.objects.get(id=id)
"""
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
"""         
class ItemCarritoDetalle(RetrieveUpdateDestroyAPIView):
    queryset = ItemCarrito.objects.all()
    serializer_class = ItemCarritoSerializer

    def get_object(self):
        # Obtenemos el valor de la URL utilizando 'self.kwargs'
        id = self.kwargs['id']
        # Usamos el filtro para encontrar el perfil correspondiente
        return ItemCarrito.objects.get(id=id)
    
class EstadoList(ListCreateAPIView):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    
    def get_object(self):
        # Obtenemos el valor de la URL utilizando 'self.kwargs'
        id = self.kwargs['id']
        # Usamos el filtro para encontrar el perfil correspondiente
        return Estado.objects.get(id=id)
    
    def post_serializer_class(self):
        if self.request.method == 'POST':
            return Response(EstadoSerializer)
        else:
            return Response({"error": "No se ha podido realizar la request"},status=status.HTTP_405_METHOD_NOT_ALLOWED,)
    
class EstadoDetalle(RetrieveUpdateDestroyAPIView):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    
    def get_object(self):
        # Obtenemos el valor de la URL utilizando 'self.kwargs'
        id = self.kwargs['id']
        # Usamos el filtro para encontrar el perfil correspondiente
        return Estado.objects.get(id=id)
    
class PedidoList(ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    
    def get_object(self):
        # Obtenemos el valor de la URL utilizando 'self.kwargs'
        id = self.kwargs['id']
        # Usamos el filtro para encontrar el perfil correspondiente
        return Pedido.objects.get(id=id)
    
    def post_serializer_class(self):
        if self.request.method == 'POST':
            return Response(PedidoSerializer)
        else:
            return Response({"error": "No se ha podido realizar la request"},status=status.HTTP_405_METHOD_NOT_ALLOWED,)

class PedidoDetalle(RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    
    def get_object(self):
        # Obtenemos el valor de la URL utilizando 'self.kwargs'
        id = self.kwargs['id']
        # Usamos el filtro para encontrar el perfil correspondiente
        return Pedido.objects.get(id=id)

class DetallePedidoList(ListCreateAPIView):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
    
    def get_object(self):
        # Obtenemos el valor de la URL utilizando 'self.kwargs'
        id = self.kwargs['id']
        # Usamos el filtro para encontrar el perfil correspondiente
        return DetallePedido.objects.get(id=id)
    
    def post_serializer_class(self):
        if self.request.method == 'POST':
            return Response(DetallePedidoSerializer)
        else:
            return Response({"error": "No se ha podido realizar la request"},status=status.HTTP_405_METHOD_NOT_ALLOWED,)

class DetallePedidoDetalle(RetrieveUpdateDestroyAPIView):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
    
    def get_object(self):
        # Obtenemos el valor de la URL utilizando 'self.kwargs'
        id = self.kwargs['id']
        # Usamos el filtro para encontrar el perfil correspondiente
        return DetallePedido.objects.get(id=id)

class MetodoPagoList(ListCreateAPIView):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer
    
    def get_object(self):
        # Obtenemos el valor de la URL utilizando 'self.kwargs'
        id = self.kwargs['id']
        # Usamos el filtro para encontrar el perfil correspondiente
        return MetodoPago.objects.get(id=id)
    
    def post_serializer_class(self):
        if self.request.method == 'POST':
            return Response(MetodoPagoSerializer)
        else:
            return Response({"error": "No se ha podido realizar la request"},status=status.HTTP_405_METHOD_NOT_ALLOWED,)

class MetodoPagoDetalle(RetrieveUpdateDestroyAPIView):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer
    
    def get_object(self):
        # Obtenemos el valor de la URL utilizando 'self.kwargs'
        id = self.kwargs['id']
        # Usamos el filtro para encontrar el perfil correspondiente
        return MetodoPago.objects.get(id=id)
    
def payment(request):
    # pedido = Pedido.objects.get(id_pedido=pedido_id)
    
    # #comprobar si existe un pago para el pedido
    # if Pago.objects.filter(pedido=pedido).exists():
    #     return HttpResponse('Este pedido ya tiene un pago asociado.', status=400)

    # Preparas los parámetros para la API
    params = {
        "buy_order": 123,
        "session_id": 123,
        "amount": 12900,
        "return_url": "http://127.0.0.1:8000/verify_transaction"
    }
    
    headers = {
        "Tbk-Api-Key-Id": "597055555532",
        "Tbk-Api-Key-Secret": "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C",
        "Content-Type": "application/json"
    }

    # Haces la llamada a la API
    response = requests.post('https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions', headers=headers, json=params)

    # Si la respuesta es exitosa, obtienes el token y renderizas la página de pago
    if response.status_code == 200:
        token = response.json()['token']
        return render(request, 'payment.html', {'token': token, 'message': 'Proceder al pago', 'submit': 'Pagar'})
    else:
        print(response.text)
        return HttpResponseBadRequest()
    
@csrf_exempt
def verify_transaction(request):
    if request.method == 'POST':
        response = request.POST

        return render(request, 'response.html', {'response': response})
    elif request.method == 'GET':
        # Capturas el token de la URL
        token = request.GET.get('token_ws')

        url = f"https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/{token}"
        headers = {
            "Tbk-Api-Key-Id": "597055555532",
            "Tbk-Api-Key-Secret": "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C",
            "Content-Type": "application/json"
        }
        
        response = requests.put(url, headers=headers)
        
        # Crear un pago
        response_data = response.json()
        # pago_data = {
        #     'pedido': response_data['buy_order'],
        #     'metodo_pago': response_data['payment_type_code'],
        #     'monto': response_data['amount'],
        #     'estado_pago': response_data['response_code'],
            
        # }
        # serializer = PagoSerializer(data=pago_data)
        # if serializer.is_valid():
        #     pago = serializer.save()
        # else:
        #     return HttpResponseBadRequest(serializer.errors)

        # #crear la transaccion
        # transaccion_data = {
        #     'pedido': pago.pedido.id_pedido,
        #     'cliente': pago.pedido.usuario.id,
        #     'pago': pago.id_pago,
        # }
        # transaccion_serializer = TransaccionSerializer(data=transaccion_data)
        # if transaccion_serializer.is_valid():
        #     transaccion_serializer.save()
        # else:
        #     raise serializers.ValidationError(transaccion_serializer.errors)
        
        return render(request, 'response.html', {'response': response_data})
    else:
        return HttpResponseBadRequest()