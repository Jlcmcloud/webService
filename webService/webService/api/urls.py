from api.views import *
from django.urls import re_path as url,path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    url(r'get-token/$', ObtainTokenView.as_view(), name='get-token'),
    url(r'^api/productos/$',ProductoList.as_view(),name='producto-list'),
    url(r'^api/productos/(?P<id>[\w.-]+)/$', ProductoDetail.as_view(), name='producto-detail'),
    url(r'^api/clientes/$',ClienteList.as_view(),name='cliente-list'),
    url(r'^api/clientes/(?P<id>[\w.-]+)/$', ClienteDetalle.as_view(), name='cliente-detail'),
    url(r'^api/carritos/$',CarritoList.as_view(),name='carrito-list'),
    url(r'^api/carritos/(?P<id>[\w.-]+)/$',CarritoDetalle.as_view(),name='carrito-detalle'),
    url(r'^api/itemcarrito/$',ItemCarritoList.as_view(),name='itemcarrito-list'),
    url(r'^api/itemcarrito/(?P<id>[\w.-]+)/$',ItemCarritoDetalle.as_view(),name='itemcarrito-detalle'),
    url(r'^api/estados/$',EstadoList.as_view(),name='estados-list'),
    url(r'^api/estados/(?P<id>[\w.-]+)/$',EstadoDetalle.as_view(),name='estados-detalle'),
    url(r'^api/pedidos/$',PedidoList.as_view(),name='pedidos-list'),
    url(r'^api/pedidos/(?P<id>[\w.-]+)/$',PedidoDetalle.as_view(),name='pedidos-detalle'),    
    url(r'^api/detallepedidos/$',DetallePedidoList.as_view(),name='detallepedido-list'),
    url(r'^api/detallepedidos/(?P<id>[\w.-]+)/$',DetallePedidoDetalle.as_view(),name='detallepedido-detalle'),    
    url(r'^api/metodopago/$',MetodoPagoList.as_view(),name='metodopago-list'),
    url(r'^api/metodopago/(?P<id>[\w.-]+)/$',MetodoPagoDetalle.as_view(),name='metodopago-detalle'),        
    path('payment/', payment, name='payment'),
    url(r'verify_transaction', verify_transaction, name='verify_transaction'),
    url(r'^login/$', login, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^perfil/$', perfil, name='perfil'),
    
]
    


urlpatterns = format_suffix_patterns(urlpatterns)