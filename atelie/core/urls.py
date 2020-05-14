
from django.urls import path
from .views import Home, Venda, Consulta, Produto, consultaProd
urlpatterns = [
    path('', Home, name='index'),
    path('venda/', Venda, name='venda'),
    path('consulta/', Consulta, name='consulta'),
    path('produto/', Produto, name='produto'),
    path('produto/', consultaProd, name='consultaprod')

]