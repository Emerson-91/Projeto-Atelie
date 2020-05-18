from django.shortcuts import render
from .forms import *

from datetime import datetime



def Home(request):
    template = "index.html"
    context = {}
    return render(request, template, context)

def Venda(request):
    form = CadastroForm()
    listProd = CadProduto.objects.all()
    if request.method == 'POST':
        formPOST = CadastroForm(request.POST)
        if formPOST.is_valid():
            formPOST.save()
            return render(request, 'venda.html', {'form': form, 'listProd':listProd})
        else:
            return render(request, 'venda.html', {'form': formPOST, 'listProd':listProd})
    else:
        return render(request, 'venda.html', {'form': form, 'listProd':listProd})


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
       list = list.filter(data_pedido__range=(dI, dF))  # BUSCANDO PELA DATA OK
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


def pedido(request):

    return render(request, 'pedido.html')
