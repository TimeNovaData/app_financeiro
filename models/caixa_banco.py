from django.db import models

from .tipo_conta import TipoConta


class CaixaBanco(models.Model):
    """
    A classe CaixaBanco serve para registrarmos
    os caixas de um banco (uma conta de um banco).

    Além de fazer as implementações relacionadas
    a uma única caixa.
    """

    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
    )

    tipo_conta = models.ForeignKey(
        TipoConta,
        verbose_name="Tipo de conta",
        null=True,
        on_delete=models.SET_NULL,
    )

    periodo_abertura = models.DateField(
        verbose_name="Período de abertura",
        null=True,
    )

    periodo_encerramento = models.DateField(
        verbose_name="Período de encerramento",
        null=True,
        blank=True,
    )

    considerar_fluxo_caixa = models.BooleanField(
        verbose_name="Considerar fluxo de caixa?",
        default=True,
    )

    nao_aceita_lancamentos = models.BooleanField(
        verbose_name="Não aceita lançamentos?",
        default=False,
    )

    @property
    def periodo_completo(self):
        if self.periodo_abertura and self.periodo_encerramento:
            periodo_abertura = self.periodo_abertura.strftime("%d/%m/%Y")
            periodo_encerramento = self.periodo_encerramento.strftime(
                "%d/%m/%Y"
            )
            return f"{periodo_abertura} - {periodo_encerramento}"
        else:
            return "Períodos não definidos"

    periodo_completo.fget.short_description = "Período completo"  # type:ignore
    periodo_completo.fget.admin_order_field = "periodo_abertura"  # type:ignore

    @property
    def considerar_fluxo_caixa_str(self):
        return "Sim" if self.considerar_fluxo_caixa else "Não"

    @property
    def aceita_lancamentos_str(self):
        return "Não" if self.nao_aceita_lancamentos else "Sim"

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "financeiro"
        verbose_name = "Caixa de banco"
        verbose_name_plural = "Caixas de banco"
