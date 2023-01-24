from core.admin import BaseNovadataAdmin
from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedOnlyDropdownFilter

from ..models import Parcela


@admin.register(Parcela)
class ParcelaAdmin(BaseNovadataAdmin):
    list_display = [
        "id",
        "lancamento_financeiro",
        "data_vencimento",
        "data_pagamento",
        "valor",
        "valor_efetivo",
        "caixa_banco_real",
        "conta_gerencial",
    ]

    search_fields = [
        "id",
        "lancamento_financeiro__empresa__nome",
        "lancamento_financeiro__tipo",
        "lancamento_financeiro__valor_total",
        "data_vencimento",
        "data_pagamento",
        "valor",
        "valor_efetivo",
        "caixa_banco_real__nome",
        "conta_gerencial__nome",
    ]

    list_filter = [
        ("lancamento_financeiro", RelatedOnlyDropdownFilter),
        "data_vencimento",
        "data_pagamento",
        "caixa_banco_real",
        "conta_gerencial",
    ]

    autocomplete_fields = [
        "lancamento_financeiro",
        "caixa_banco_real",
        "conta_gerencial",
    ]

    list_select_related = [
        "lancamento_financeiro__empresa",
        "caixa_banco_real",
        "conta_gerencial",
    ]

    readonly_fields = [
        "valor_efetivo",
    ]

    fieldsets = [
        (
            "Dados principais",
            {
                "fields": [
                    "lancamento_financeiro",
                    "caixa_banco_real",
                    "conta_gerencial",
                ]
            },
        ),
        (
            "Datas",
            {
                "fields": [
                    "data_referencia",
                    "data_vencimento",
                    "data_pagamento",
                ]
            },
        ),
        (
            "Valores",
            {
                "fields": [
                    "valor",
                    "acrescimo",
                    "desconto",
                    "valor_efetivo",
                ]
            },
        ),
    ]

    actions = [
        "pagar",
    ]

    def pagar(self, request, queryset):
        """
        Marca as parcelas selecionadas como pagas.
        """

        for parcela in queryset:
            parcela.pagar()
