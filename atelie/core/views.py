from django.shortcuts import render
from django.shortcuts import HttpResponse

def Venda(request):
    template = "venda.html"
    context = { }
    return render(request, template, context)

def Home(request):
    msg = "Teste Ola Mundo!"
    template = "index.html"
    context = {'msg': msg, }
    return render(request, template, context)


def Consulta(request):
    template = "consulta.html"
    context = {}
    return render(request, template, context)

def Produto(request):
    return HttpResponse('<h1> Cadastro de Produtos </h1>')