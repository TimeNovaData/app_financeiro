from django.db import models

from .banco import Banco


class DadoBancario(models.Model):
    """
    A classe DadoBancario é um modelo de dados
    que representa os dados bancários de um fornecedor.

    Serve também para fazer as implementações referentes
    a um único dado bancário.
    """

    banco = models.ForeignKey(
        Banco,
        verbose_name="Banco",
        null=True,
        on_delete=models.CASCADE,
    )

    agencia = models.CharField(
        verbose_name="Agência",
        max_length=5,
    )

    conta = models.CharField(
        verbose_name="Conta",
        max_length=10,
    )

    caixa_banco = models.OneToOneField(
        "financeiro.CaixaBanco",  # Evitando circular import
        verbose_name="Caixa de banco",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.banco} - {self.agencia} - {self.conta}"

    class Meta:
        app_label = "financeiro"
        verbose_name = "Dado bancário"
        verbose_name_plural = "Dados bancários"
