from core.admin import BaseNovadataAdmin
from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedOnlyDropdownFilter

from ..models import Rateio

from .item_rateio_inline import ItemRateioInline


@admin.register(Rateio)
class RateioAdmin(BaseNovadataAdmin):
    list_display = [
        "id",
        "nome",
        "valor",
        "numero_parcelas",
        #
        "tipo",
        "empresa",
        "conta_gerencial",
        "tipo_documento",
        "conta_caixa",
        "data_referencia",
    ]

    search_fields = [
        "id",
        "nome",
        "valor",
        "tipo",
        "numero_parcelas",
        "empresa__nome",
        "conta_gerencial__nome",
        "tipo_documento__nome",
        "conta_caixa__nome",
        "data_referencia",
    ]

    list_filter = [
        "tipo",
        "numero_parcelas",
        ("empresa", RelatedOnlyDropdownFilter),
        ("conta_gerencial", RelatedOnlyDropdownFilter),
        ("tipo_documento", RelatedOnlyDropdownFilter),
        ("conta_caixa", RelatedOnlyDropdownFilter),
        "data_referencia",
    ]

    autocomplete_fields = [
        "empresa",
        "conta_gerencial",
        "tipo_documento",
        "conta_caixa",
    ]

    inlines = [
        ItemRateioInline,
    ]

    fieldsets = [
        (
            "Dados principais",
            {
                "fields": [
                    "nome",
                    "valor",
                    "numero_parcelas",
                ]
            },
        ),
        (
            "Dados do lançamento",
            {
                "fields": [
                    "tipo",
                    "empresa",
                    "conta_gerencial",
                    "tipo_documento",
                    "conta_caixa",
                    "data_referencia",
                ]
            },
        ),
    ]

    def has_add_permission(self, request) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False
