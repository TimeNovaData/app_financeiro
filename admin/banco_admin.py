from core.admin import BaseNovadataAdmin
from django.contrib import admin

from ..models import Banco


@admin.register(Banco)
class BancoAdmin(BaseNovadataAdmin):
    list_display = [
        'id',
        'nome',
        'codigo',
    ]

    search_fields = [
        'id',
        'nome',
        'codigo',
    ]
