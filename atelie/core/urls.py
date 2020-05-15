
from django.urls import path
from .views import Home, Venda, Consulta, Produto
urlpatterns = [
    path('', Home, name='index'),
    path('venda/', Venda, name='venda'),
    path('consulta/', Consulta, name='consulta'),
    path('produto/', Produto, name='produto'),

]