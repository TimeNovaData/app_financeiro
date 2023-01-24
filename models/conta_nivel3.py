from django.db import models

from .conta_nivel2 import ContaNivel2


class ContaNivel3(models.Model):
    """
    A classe ContaGerencial3 serve para cadastrarmos e
    gerenciarmos as contas gerenciais de nível 3.

    Além de implementar as funcionalidades
    relacionadas a uma única conta.
    """

    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
    )

    conta_nivel2 = models.ForeignKey(
        ContaNivel2,
        verbose_name="Conta gerencial- Nível 2",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "financeiro"
        verbose_name = "Conta de nível 3"
        verbose_name_plural = "Contas de nível 3"
