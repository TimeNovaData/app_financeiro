from core.admin import BaseNovadataAdmin
from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedOnlyDropdownFilter

from ..models import Orcamento


@admin.register(Orcamento)
class OrcamentoAdmin(BaseNovadataAdmin):
    list_display = [
        'id',
        'ano_contabil',
        'conta_gerencial2',
        'valor_orcamento',
    ]

    search_fields = [
        'id',
        'ano_contabil__nome',
        'conta_gerencial2__nome',
        'valor_orcamento',
    ]

    list_filter = [
        ('ano_contabil', RelatedOnlyDropdownFilter),
        ('conta_gerencial2', RelatedOnlyDropdownFilter),
    ]

    autocomplete_fields = [
        'ano_contabil',
        'conta_gerencial2',
    ]

    list_select_related = [
        'ano_contabil',
    ]
