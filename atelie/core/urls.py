
from django.urls import path
from .views import Home, Venda, Consulta, Produto, pedido, update
urlpatterns = [
    path('', Home, name='index'),
    path('venda/', Venda, name='venda'),
    path('consulta/', Consulta, name='consulta'),
    path('produto/', Produto, name='produto'),
    path('pedido/<int:pk>/', pedido, name='pedido'),
    path('update/<int:pk>/', update, name='update'),

]