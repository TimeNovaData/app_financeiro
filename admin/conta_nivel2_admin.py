from core.admin import BaseNovadataAdmin
from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedOnlyDropdownFilter

from ..models import ContaNivel2
from .conta_nivel3_inline import ContaNivel3Inline


@admin.register(ContaNivel2)
class ContaNivel2Admin(BaseNovadataAdmin):
    list_display = [
        "id",
        "nome",
        "conta_nivel1",
    ]

    search_fields = [
        "id",
        "nome",
        "conta_nivel1__nome",
    ]

    list_filter = [
        ("conta_nivel1", RelatedOnlyDropdownFilter),
    ]

    autocomplete_fields = [
        "conta_nivel1",
    ]

    list_select_related = [
        "conta_nivel1",
    ]

    inlines = [
        ContaNivel3Inline,
    ]
