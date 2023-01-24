from core.admin import BaseNovadataAdmin
from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedOnlyDropdownFilter

from ..models import LancamentoFinanceiro
from .log_alteracoes_lancamento_financeiro_inline import (
    LogAlteracoesLancamentoFinanceiroInline,
)
from .parcela_inline import ParcelaInline


@admin.register(LancamentoFinanceiro)
class LancamentoFinanceiroAdmin(BaseNovadataAdmin):
    list_display = [
        "id",
        "compra",
        "empresa",
        "conta_gerencial",
        "tipo_documento",
        "destinacao",
        "data_vencimento",
        "valor_total",
        "valor_pendente",
        "forma_pagamento",
        "tipo",
    ]

    search_fields = [
        "id",
        "compra__id",
        "empresa__nome",
        "conta_gerencial__nome",
        "tipo_documento__nome",
        "destinacao",
        "valor_total",
        "forma_pagamento",
        "tipo",
    ]

    list_filter = [
        ("compra", RelatedOnlyDropdownFilter),
        ("empresa", RelatedOnlyDropdownFilter),
        ("conta_gerencial", RelatedOnlyDropdownFilter),
        ("tipo_documento", RelatedOnlyDropdownFilter),
        "destinacao",
        "forma_pagamento",
        "tipo",
    ]

    autocomplete_fields = [
        "compra",
        "empresa",
        "conta_gerencial",
        "tipo_documento",
        "conta_caixa",
    ]

    list_select_related = [
        "empresa",
        "conta_gerencial",
        "tipo_documento",
        "conta_caixa",
    ]

    readonly_fields = [
        "data_vencimento",
        "valor_pendente",
        "valor_pago",
    ]

    fieldsets = [
        (
            "Dados principais",
            {
                "fields": [
                    "compra",
                    "empresa",
                    "conta_gerencial",
                    "conta_caixa",
                    "destinacao",
                ]
            },
        ),
        (
            "Detalhes",
            {
                "fields": [
                    "numero_nota_fiscal",
                    "observacoes_nota_fiscal",
                    "tipo",
                    "tipo_documento",
                    "anotacoes",
                ]
            },
        ),
        (
            "Pagamento",
            {
                "fields": [
                    "data_referencia",
                    "data_referencia_parcelas",
                    "data_vencimento",
                    "valor_total",
                    "impostos",
                    "valor_pago",
                    "valor_pendente",
                    "forma_pagamento",
                ]
            },
        ),
    ]

    inlines = [
        ParcelaInline,
        LogAlteracoesLancamentoFinanceiroInline,
    ]
