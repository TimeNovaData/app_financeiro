from core.admin import BaseNovadataAdmin
from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedOnlyDropdownFilter

from ..models import CaixaBanco
from .dado_bancario_inline import DadoBancarioInline


@admin.register(CaixaBanco)
class CaixaBancoAdmin(BaseNovadataAdmin):
    list_display = [
        "id",
        "nome",
        "tipo_conta",
        "periodo_completo",
        "dadobancario",
        "considerar_fluxo_caixa",
        "gerar_remessa_pagamento",
        "nao_aceita_lancamentos",
    ]

    search_fields = [
        "id",
        "nome",
        "tipo_conta__nome",
        "periodo_abertura",
        "periodo_encerramento",
        "dadobancario__banco__nome",
        "dadobancario__empresa__nome",
        "considerar_fluxo_caixa",
        "gerar_remessa_pagamento",
        "nao_aceita_lancamentos",
    ]

    list_filter = [
        ("tipo_conta", RelatedOnlyDropdownFilter),
        ("dadobancario", RelatedOnlyDropdownFilter),
        "considerar_fluxo_caixa",
        "gerar_remessa_pagamento",
        "nao_aceita_lancamentos",
    ]

    autocomplete_fields = [
        "tipo_conta",
    ]

    list_select_related = [
        "tipo_conta",
        "dadobancario__banco",
        "dadobancario__empresa",
    ]

    fieldsets = [
        (
            "Dados principais",
            {
                "fields": [
                    "nome",
                    "tipo_conta",
                    "periodo_abertura",
                    "periodo_encerramento",
                ]
            },
        ),
        (
            "Configurações",
            {
                "fields": [
                    "considerar_fluxo_caixa",
                    "gerar_remessa_pagamento",
                    "nao_aceita_lancamentos",
                ]
            },
        ),
    ]

    inlines = [
        DadoBancarioInline,
    ]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        is_caixa_banco_page = "caixabanco" in request.path
        if not is_caixa_banco_page:
            return queryset.filter(nao_aceita_lancamentos=True)
        return queryset

    class Media:
        js = [
            "financeiro/admin/mascaras_dado_bancario_inline.js",
            "financeiro/admin/caixa_banco_admin.js",
        ]
