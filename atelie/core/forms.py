from django import forms
from .models import *


class CadastroForm(forms.ModelForm):

    class Meta:
        model = Cadastro
        fields = ['nome', 'telefone','entrega','endereco','qtd']


class ProdutosForm(forms.ModelForm):
    class Meta:
        model = CadProduto
        fields = ['produto', 'valor']
