from core.admin import BaseNovadataAdmin
from django.contrib import admin

from ..models import FormaPagamento


@admin.register(FormaPagamento)
class FormaPagamentoAdmin(BaseNovadataAdmin):
    list_display = [
        'id',
        'nome',
    ]

    search_fields = [
        'id',
        'nome',
    ]
