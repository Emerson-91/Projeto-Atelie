from django import forms
from django_filters import DateFilter
from .models import *



class CadastroForm(forms.ModelForm):

    class Meta:
        model = Cadastro
        fields = ['nome', 'telefone','endereco', ]
        


class ProdutosForm(forms.ModelForm):
    class Meta:
        model = CadProduto
        fields = ['produto', 'valor', ]


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['produto', 'desconto', 'qtd' ]



