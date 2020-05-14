from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Cadastro
from .forms import *
from django.views.generic import CreateView, ListView

def Venda(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CadastroForm()
    return render(request, 'venda.html', {'form':form})


def Consulta(request):
    template = "consulta.html"
    List = Cadastro.objects.all()
    busca = request.GET.get('search')
    if busca:
       List = Cadastro.object.filter(nome__icontains = busca) # VERIFICAR O PROBLEMA DE NAO ESTAR BUSCANDO
    return render(request, template, {'List':List})


def consultaProd(request):
    template = "consultaprodutos.html"
    List = CadProduto.objects.all()
    return render(request, template, {'List':List})




def Produto(request):
    if request.method == 'POST':
        form = ProdutosForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProdutosForm()
    return render(request, 'produtos.html', {'form':form})


def Home(request):

    template = "index.html"
    context = { }
    return render(request, template, context)
