from core.admin import BaseNovadataAdmin
from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedOnlyDropdownFilter

from ..models import ContaNivel3


@admin.register(ContaNivel3)
class ContaNivel3Admin(BaseNovadataAdmin):
    list_display = [
        "id",
        "nome",
        "conta_nivel2",
    ]

    search_fields = [
        "id",
        "nome",
        "conta_nivel2__nome",
    ]

    list_filter = [
        ("conta_nivel2", RelatedOnlyDropdownFilter),
    ]

    autocomplete_fields = [
        "conta_nivel2",
    ]

    list_select_related = [
        "conta_nivel2",
    ]
