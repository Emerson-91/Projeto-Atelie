from django import forms
from django.forms import TextInput
from django_filters import DateFilter
from .models import *



class CadastroForm(forms.ModelForm):

    class Meta:
        model = Cadastro
        fields = ['nome', 'telefone','endereco', ]

    def __init__(self, *args, **kwargs):
        super(CadastroForm, self).__init__(*args, **kwargs)
        self.fields['telefone'].widget = TextInput(attrs={'class':'phone-mask'})



class ProdutosForm(forms.ModelForm):
    class Meta:
        model = CadProduto
        fields = ['produto', 'valor', ]


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = '__all__'


