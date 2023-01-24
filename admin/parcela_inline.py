from django.contrib import admin

from ..models import Parcela


class ParcelaInline(admin.StackedInline):
    model = Parcela

    extra = 0

    min_num = 1

    readonly_fields = [
        "valor_efetivo",
    ]

    fieldsets = [
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
