from django.db import models


# Diagramada em: 29/11/2022
class Banco(models.Model):
    """
    A classe Banco serve para registrarmos e armazenarmos todos os bancos.
    Além de realizar uma implementação relacionada a um único banco.
    """

    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
    )

    codigo = models.CharField(
        verbose_name="Código",
        max_length=10,
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "financeiro"
        verbose_name = "Banco"
        verbose_name_plural = "Bancos"
