from django.db import models
from django.conf import settings
from django.db.models import Sum


# Create your models here.
from django.db.models import CharField


class CadProduto(models.Model):
    produto = models.CharField(max_length=100)
    valor = models.FloatField(max_length=10)

    class Meta:
        db_table = 'CadProduto'

    def __str__(self):
        return self.produto


class Cadastro(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20,)
    endereco = models.CharField(default=" - ", max_length=100, blank=True)


    class Meta:
        db_table = 'Cadastro'

    def __str__(self):
        return self.nome



class Pedido(models.Model):
    ENTREGA = (('Sim', 'sim'),
               ('Nao', 'nao'),)
    STATUS_CHOICES = (
        ("A", "Aberto"),
        ("F", "Finalizado")
    )
    pedido = models.AutoField(primary_key=True)
    produto = models.ManyToManyField(CadProduto)
    cliente = models.ForeignKey(Cadastro, on_delete=models.CASCADE)
    desconto = models.FloatField(default=0)
    qtd = models.IntegerField(default=0)
    data_pedido = models.DateField(auto_now_add=True)
    entrega = models.CharField(max_length=10, choices=ENTREGA)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False)

    class Meta:
        db_table = 'pedido'

    def __str__(self):
        return self.pedido

    def get_total_item(self):
        return self.qtd * self.produto.valor

    def get_total_preco(self):
        return self.get_total_item() - self.desconto




