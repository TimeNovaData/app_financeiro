from django.db import models


class FormaPagamento(models.Model):
    """
    A classe FormaPagamento serve para armazernar os(as)
    formas de pagamento do sistema.

    Além de fazer as implementações relacionadas
    a um único objeto do tipo FormaPagamento.
    """

    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "financeiro"
        verbose_name = "Forma de pagamento"
        verbose_name_plural = "Formas de pagamento"
