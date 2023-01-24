from django.db import models


class ContaNivel1(models.Model):
    """
    A classe ContaGerencial1 serve para cadastrarmos
    e gerenciarmos as contas gerenciais de nível 1.

    Além de implementar as funcionalidades
    relacionadas a uma única conta.
    """

    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
    )

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        app_label = "financeiro"
        verbose_name = "Conta de nível 1"
        verbose_name_plural = "Contas de nível 1"
