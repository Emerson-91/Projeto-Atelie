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

def Consulta(ListView):
    template = "consulta.html"
    model = Cadastro
    context_object = 'nome'
    #return render(request, template, model, context_object)

def Produto(request):
    form = ProdutosForm()
    form.is_valid()
    form.save()
    return render(request, 'produtos.html', {'form':form})


def Home(request):

    template = "index.html"
    context = { }
    return render(request, template, context)
