from django.db import models


class TipoConta(models.Model):
    """
    A classe TipoConta serve para registrarmos
    os tipos de contas de um CaixaBanco (uma conta de banco).

    Além de fazer as implementações relacionadas
    a um único tipo de conta.
    """

    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "financeiro"
        verbose_name = "Tipo de conta"
        verbose_name_plural = "Tipos de conta"
