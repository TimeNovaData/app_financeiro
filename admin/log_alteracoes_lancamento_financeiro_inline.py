from home.admin import BaseLogAlteracoesInline

from ..models import LogAlteracoesLancamentoFinanceiro


class LogAlteracoesLancamentoFinanceiroInline(BaseLogAlteracoesInline):
    model = LogAlteracoesLancamentoFinanceiro
