from django.db import models
from home.models import BaseLogAlteracoes

from .lancamento_financeiro import LancamentoFinanceiro


class LogAlteracoesLancamentoFinanceiro(BaseLogAlteracoes):
    lancamento_financeiro = models.ForeignKey(
        LancamentoFinanceiro,
        verbose_name="Lançamento financeiro",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        default_return = f"Log de alterações {self.id}"
        lancamento = self.lancamento_financeiro

        if lancamento:
            return default_return + f"Lançamento financeiro {lancamento}"
        else:
            return default_return + "Sem lançamento financeiro"

    class Meta:
        app_label = "financeiro"
        verbose_name = "Log de alterações"
        verbose_name_plural = "Logs de alterações"
        ordering = ["-id"]
