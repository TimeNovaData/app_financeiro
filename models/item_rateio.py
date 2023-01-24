from decimal import Decimal

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .rateio import Rateio


class ItemRateio(models.Model):
    """
    A classe ItemRateio serve para armazernar
    os(as) itens de rateio do sistema.

    Além de fazer as implementações relacionadas
    a um único objeto do tipo ItemRateio.
    """

    porcentagem = models.DecimalField(
        verbose_name="Porcentagem",
        max_digits=5,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal("0.01")),
            MaxValueValidator(100),
        ],
    )

    valor = models.DecimalField(
        verbose_name="Valor",
        max_digits=15,
        decimal_places=2,
        null=True,
        validators=[
            MinValueValidator(Decimal("0.01")),
        ],
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data de criação",
        auto_now_add=True,
        null=True,
    )

    @property
    def has_lancamento_finaneiro(self):
        return hasattr(self, "lancamentofinanceiro")

    def __str__(self):
        return f"Item de rateio {self.id}"

    class Meta:
        app_label = "financeiro"
        verbose_name = "Item de rateio"
        verbose_name_plural = "Itens de rateio"
