from django.db import models

# Create your models here.
class CadProduto(models.Model):
    produto = models.CharField(max_length=100)
    valor = models.CharField(max_length=10)

class Cadastro(models.Model):
    ENTREGA = (( 'Sim', 'sim'),
    ('Nao', 'nao'),)
    pedido = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20,)
    endereco = models.CharField(max_length=100, blank=True)
    data_pedido = models.DateTimeField('data do pedido', auto_now_add=True)
    entrega = models.CharField(max_length=10, choices=ENTREGA)
    qtd = models.IntegerField(default=0)
    prod_id = models.ForeignKey(CadProduto, null=True, related_name='produtos', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

