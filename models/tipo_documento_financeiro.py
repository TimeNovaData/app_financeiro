from django.db import models


class TipoDocumentoFinanceiro(models.Model):
    """
    A classe TipoDocumentoFinanceiro serve para
    armazernar os(as) tipos dedocumento financeiro do sistema.

    Além de fazer as implementações relacionadas
    a um único objeto do tipo TipoDocumentoFinanceiro.
    """

    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
    )

    codigo = models.CharField(
        verbose_name="Código",
        max_length=15,
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "financeiro"
        verbose_name = "Tipo de documento financeiro"
        verbose_name_plural = "Tipos de documento financeiro"
        ordering = ["-id"]
