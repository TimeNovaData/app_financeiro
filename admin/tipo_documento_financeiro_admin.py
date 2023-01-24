from core.admin import BaseNovadataAdmin
from django.contrib import admin

from ..models import TipoDocumentoFinanceiro


@admin.register(TipoDocumentoFinanceiro)
class TipoDocumentoFinanceiroAdmin(BaseNovadataAdmin):
    list_display = [
        "id",
        "codigo",
        "nome",
    ]

    search_fields = [
        "id",
        "codigo",
        "nome",
    ]
