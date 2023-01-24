from core.admin import BaseNovadataAdmin
from django.contrib import admin


from ..models import AnoContabil


@admin.register(AnoContabil)
class AnoContabilAdmin(BaseNovadataAdmin):
    list_display = [
        "id",
        "nome",
        "data_inicial",
        "data_final",
        "aberto",
    ]

    search_fields = [
        "id",
        "nome",
        "data_inicial",
        "data_final",
    ]

    list_filter = [
        "aberto",
    ]
