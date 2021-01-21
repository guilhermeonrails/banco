from django.db import models
from django.db.models import F

class Contas(models.Model):
    agencia = models.CharField(max_length=10)
    conta = models.CharField(max_length=6)
    saldo = models.DecimalField(decimal_places=2, max_digits=30, default=0.00)
    ultima_movimentacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{str(self.agencia)}/{str(self.conta)}'

    def get_ultima_movimentacao(self):
        return self.ultima_movimentacao.strftime('%d/%m/%Y %H:%M')

class Deposito(models.Model):
    conta = models.ForeignKey('Contas', on_delete=models.CASCADE)
    valor = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    data_deposito = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.conta)}'

    def get_data_deposito(self):
        return self.data_deposito.strftime('%d/%m/%Y %H:%M')

    def get_saldo_atualizado(self):
        novo_saldo = self.conta.saldo + self.valor
        return novo_saldo

    def save(self, *args, **kwargs):
        if not self.pk:
            Contas.objects.filter(pk=self.conta_id).update(saldo=F('saldo')+ self.valor)
        super().save(*args, **kwargs)