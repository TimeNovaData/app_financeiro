from django.contrib import admin

from ..models import LancamentoFinanceiro


class LancamentoFinanceiroInline(admin.StackedInline):
    model = LancamentoFinanceiro

    extra = 0

    classes = [
        "collapse",
    ]

    readonly_fields = [
        "valor_pendente",
        "conta_caixa",
    ]

    autocomplete_fields = [
        "conta_gerencial",
        # 'conta_caixa',
        "tipo_documento",
        "empresa",
        # "termo_cooperacao",
        "forma_pagamento",
    ]

    fieldsets = [
        (
            "Dados principais",
            {
                "fields": [
                    "conta_gerencial",
                    "conta_caixa",
                    "tipo_documento",
                    "empresas",
                    # "termo_cooperacao",
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
                    "anotacoes",
                ]
            },
        ),
        (
            "Pagamento",
            {
                "fields": [
                    "data_referencia",
                    # 'data_vencimento',
                    "valor_total",
                    # 'valor_pago',
                    "valor_pendente",
                    "forma_pagamento",
                ]
            },
        ),
        (
            "Impostos",
            {
                "fields": [
                    "impostos",
                ]
            },
        ),
    ]
