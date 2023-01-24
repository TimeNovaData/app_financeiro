from django.db import models

from .conta_nivel3 import ContaNivel3


class ContaNivel4(models.Model):
    """
    A classe ContaGerencial4 servepara cadastrarmos
    e gerenciarmos as contas gerenciais de nível 4.

    Além de implementar as funcionalidades
    relacionadas a uma única conta.
    """

    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
    )

    conta_nivel3 = models.ForeignKey(
        ContaNivel3,
        verbose_name="Conta gerencial- Nível 3",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "financeiro"
        verbose_name = "Conta de nível 4"
        verbose_name_plural = "Contas de nível 4"
