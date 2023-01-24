from core.admin import BaseNovadataAdmin
from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedOnlyDropdownFilter

from ..models import ItemRateio


# @admin.register(ItemRateio)
class ItemRateioAdmin(BaseNovadataAdmin):
    list_display = [
        "id",
        "rateio",
        "empresa",
        "termo_cooperacao",
        "porcentagem",
        "valor",
    ]

    search_fields = [
        "id",
        "rateio",
        "empresa",
        "termo_cooperacao",
        "porcentagem",
        "valor",
    ]

    list_filter = [
        ("rateio", RelatedOnlyDropdownFilter),
        ("empresa", RelatedOnlyDropdownFilter),
        ("termo_cooperacao", RelatedOnlyDropdownFilter),
    ]

    list_select_related = [
        "rateio",
        "empresa",
        "termo_cooperacao",
    ]

    autocomplete_fields = [
        "rateio",
        "empresa",
        "termo_cooperacao",
    ]

    readonly_fields = [
        "saldo_termo_cooperacao",
    ]
