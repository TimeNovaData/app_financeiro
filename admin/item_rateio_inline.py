from django.contrib import admin

from ..models import ItemRateio


class ItemRateioInline(admin.TabularInline):
    model = ItemRateio

    extra = 0

    readonly_fields = [
        "saldo_termo_cooperacao",
    ]

    autocomplete_fields = [
        "termo_cooperacao",
    ]
