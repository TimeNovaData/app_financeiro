from core.admin import BaseNovadataAdmin
from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedOnlyDropdownFilter

from ..models import DadoBancario


# @admin.register(DadoBancario)
class DadoBancarioAdmin(BaseNovadataAdmin):
    list_display = [
        "id",
        "banco",
        "agencia",
        "conta",
        "fornecedor",
        "empresa",
        "empresa",
    ]

    search_fields = [
        "id",
        "banco__nome",
        "agencia",
        "conta",
        "fornecedor__nome",
        "empresa__nome",
        "empresa__nome",
    ]

    list_filter = [
        ("banco", RelatedOnlyDropdownFilter),
        ("fornecedor", RelatedOnlyDropdownFilter),
        ("empresa", RelatedOnlyDropdownFilter),
        ("empresa", RelatedOnlyDropdownFilter),
    ]

    autocomplete_fields = [
        "banco",
        "fornecedor",
        "empresa",
        "empresa",
    ]

    list_select_related = [
        "banco",
        "fornecedor",
        "empresa",
        "empresa",
    ]

    readonly_fields = [
        "banco",
        "agencia",
        "conta",
        "fornecedor",
        "empresa",
        "empresa",
    ]

    fieldsets = [
        (
            "Dados principais",
            {
                "fields": [
                    "banco",
                    "agencia",
                    "conta",
                ]
            },
        ),
        (
            "Pessoas",
            {
                "fields": [
                    "fornecedor",
                    "empresa",
                    "empresa",
                ]
            },
        ),
    ]

    def has_add_permission(self, request):
        return False

    class Media:
        js = [
            "financeiro/admin/mascaras_dado_bancario.js",
            "financeiro/admin/dado_bancario.js",
        ]
