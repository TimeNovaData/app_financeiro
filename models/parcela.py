from django.db import models

from .caixa_banco import CaixaBanco
from .conta_nivel4 import ContaNivel4
from .lancamento_financeiro import LancamentoFinanceiro


class Parcela(models.Model):
    """
    A classe Parcela serve para armazernar os(as) parcelas do sistema.
    Além de fazer as implementações relacionadas a um
    único objeto do tipo Parcela.
    """

    lancamento_financeiro = models.ForeignKey(
        LancamentoFinanceiro,
        verbose_name="Lançamento financeiro",
        on_delete=models.CASCADE,
    )

    data_referencia = models.DateField(
        verbose_name="Data de referência",
        null=True,
        blank=True,
    )

    data_vencimento = models.DateField(
        verbose_name="Data de vencimento",
    )

    data_pagamento = models.DateField(
        verbose_name="Data de pagamento",
        null=True,
        blank=True,
    )

    valor = models.DecimalField(
        verbose_name="Valor",
        max_digits=15,
        decimal_places=2,
    )

    acrescimo = models.DecimalField(
        verbose_name="Acréscimo",
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True,
    )

    desconto = models.DecimalField(
        verbose_name="Desconto",
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True,
    )

    caixa_banco_real = models.ForeignKey(
        CaixaBanco,
        verbose_name="Caixa/banco real",
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={"nao_aceita_lancamentos": False},
    )

    conta_gerencial = models.ForeignKey(
        ContaNivel4,
        verbose_name="Conta gerencial",
        on_delete=models.SET_NULL,
        null=True,
    )

    observacoes = models.TextField(
        verbose_name="Observações",
        null=True,
        blank=True,
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data de criação",
        auto_now_add=True,
        null=True,
    )

    @property
    def valor_efetivo(self):
        # O or 0 é para caso não exista o valor.
        return (self.valor or 0) + (self.acrescimo or 0) - (self.desconto or 0)

    @property
    def paga(self):
        return self.data_pagamento is not None

    @property
    def paga_str(self):
        return "Sim" if self.paga else "Não"

    def pagar(self, pagar_parcela_form):
        """
        Marca a parcela como paga.
        """

        if not self.data_pagamento and pagar_parcela_form.is_valid():
            pagar_parcela_form.save()

    def __str__(self):
        if self.lancamento_financeiro and self.data_vencimento:
            return f"{self.lancamento_financeiro} - {self.data_vencimento}"
        else:
            return "Favor informar um lançamento e uma data de vencimento"

    class Meta:
        app_label = "financeiro"
        verbose_name = "Parcela"
        verbose_name_plural = "Parcelas"
        ordering = ["data_vencimento"]
