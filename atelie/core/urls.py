
from django.urls import path

from . import views
from .views import Home, Cliente, Consulta, Produto, pedido, update, venda, updatecliente, deletaproduto
urlpatterns = [
    path('', Home, name='index'),
    path('cliente/', Cliente, name='cliente'),
    path('consulta/', Consulta, name='consulta'),
    path('venda/', venda, name='venda'),
    path('produto/', Produto, name='produto'),
    path('pedido/<int:pk>/', pedido, name='pedido'),
    path('produto/<int:pk>/', update, name='update'),
    path('produto/<int:pk>/', deletaproduto, name='deletaproduto'),
    path('cliente/<int:pk>/', updatecliente, name='updatecliente'),

]