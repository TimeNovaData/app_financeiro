from core.admin import BaseNovadataAdmin
from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedOnlyDropdownFilter

from ..models import TipoConta


@admin.register(TipoConta)
class TipoContaAdmin(BaseNovadataAdmin):
    list_display = [
        "id",
        "nome",
    ]

    search_fields = [
        "id",
        "nome",
    ]
