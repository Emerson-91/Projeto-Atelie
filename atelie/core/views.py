from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Cadastro
from .forms import *

from datetime import datetime
from django.views.generic import CreateView, ListView


def Venda(request):
    form = CadastroForm()
    if request.method == 'POST':
        formPOST = CadastroForm(request.POST)
        if formPOST.is_valid():
            formPOST.save()
            return render(request, 'venda.html', {'form': form})
        else:
            return render(request, 'venda.html', {'form': formPOST})
    else:
        return render(request, 'venda.html', {'form': form})


def Consulta(request):
    template = "consulta.html"
    list = Cadastro.objects.all()
    buscanome = request.GET.get('searchnome')
    buscapedido = request.GET.get('searchnr')
    datainicial = request.GET.get('data_inicial')
    datafinal = request.GET.get('data_final')
    if buscanome:
        list = list.filter(nome__icontains=buscanome)  #  Buscando pelo nome OK
        return render(request, template, {'list': list})
    if buscapedido:
        list = list.filter(pedido__icontains=buscapedido)  # Buscando pelo Nr Pedido OK
        return render(request, template, {'list': list})
    if datainicial and datafinal:
       dI = datetime.strptime(datainicial, "%Y-%m-%d")
       dF = datetime.strptime(datafinal, "%Y-%m-%d")
       list = list.filter(data_pedido__range=(dI, dF))  # VERIFICAR O PROBLEMA DE NAO ESTAR BUSCANDO
       return render(request, template, {'list': list})
    return render(request, template, {'list': list})



def Produto(request):
    form = ProdutosForm()
    ListProd = CadProduto.objects.all()

    if request.method == 'POST':
        formPOST = ProdutosForm(request.POST)
        if formPOST.is_valid():
            formPOST.save()
            return render(request, 'produtos.html', {'form': form, 'ListProd': ListProd})
        else:
            return render(request, 'produtos.html', {'form': formPOST, 'ListProd': ListProd})
    else:
        return render(request, 'produtos.html', {'form': form, 'ListProd': ListProd})


def Home(request):
    template = "index.html"
    context = {}
    return render(request, template, context)
