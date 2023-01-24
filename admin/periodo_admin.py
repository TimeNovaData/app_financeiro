from core.admin import BaseNovadataAdmin
from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedOnlyDropdownFilter

from ..models import Periodo


# @admin.register(Periodo)
class PeriodoAdmin(BaseNovadataAdmin):
    list_display = [
        "id",
        "nome",
        "data_inicial",
        "data_final",
        "aberto",
        "ano_contabil",
    ]

    search_fields = [
        "id",
        "nome",
        "data_inicial",
        "data_final",
        "ano_contabil__nome",
    ]

    list_filter = [
        "aberto",
        ("ano_contabil", RelatedOnlyDropdownFilter),
    ]

    autocomplete_fields = [
        "ano_contabil",
    ]

    list_select_related = [
        "ano_contabil",
    ]
