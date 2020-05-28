from django.shortcuts import render, redirect
from .forms import *

from datetime import datetime



def Home(request):
    template = "index.html"
    context = {}
    return render(request, template, context)

def Cliente(request):
    list = Cadastro.objects.all()
    form = CadastroForm()
    if request.method == 'POST':
       formPOST = CadastroForm(request.POST)
       if formPOST.is_valid():
          formPOST.save()
          return render(request, 'cliente.html', {'form': form, 'list':list})
       else:
          return render(request, 'cliente.html', {'form': formPOST, 'list':list})
    else:
          return render(request, 'cliente.html', {'form': form, 'list':list})


def updatecliente(request, pk, *args, **kwargs):
    cliente = Cadastro.objects.get(pk=pk)
    form = CadastroForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('/projeto/cliente/')

    return render(request, 'cliente.html', {'form':form})


def venda(request):

    return render(request, 'venda.html')

def Consulta(request):
    template = "consulta.html"
    list = Cadastro.objects.all()
    buscanome = request.GET.get('searchnome')
    buscapedido = request.GET.get('searchnr')
    datainicial = request.GET.get('data_inicial')
    datafinal = request.GET.get('data_final')
    entrega = request.GET.get('entrega')
    if entrega:
        list = list.filter(entrega__icontains=entrega)
        return render(request, template, {'list': list})

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


def pedido(request, pk, *args, **kwargs):
    produto = Cadastro.objects.get(pk=pk,)
    return render(request, 'pedido.html', {'produto': produto})


def update(request, pk):
    produto = CadProduto.objects.get(pk=pk)
    form = ProdutosForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('/projeto/produto/')

    return render(request, 'produtos.html', {'form':form})

