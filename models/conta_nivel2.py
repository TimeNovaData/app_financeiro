from django.db import models

from .conta_nivel1 import ContaNivel1


class ContaNivel2(models.Model):
    """
    A classe ContaNivel2 serve para cadastrarmos e
    gerenciarmos as contas gerenciais de nível 2.

    Além de implementar as funcionalidades
    relacionadas a uma única conta.
    """

    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
    )

    conta_nivel1 = models.ForeignKey(
        ContaNivel1,
        verbose_name="Conta gerencial - Nível 1",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "financeiro"
        verbose_name = "Conta de nível 2"
        verbose_name_plural = "Contas de nível 2"
