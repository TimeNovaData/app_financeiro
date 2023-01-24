from core.admin import BaseNovadataAdmin
from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedOnlyDropdownFilter

from ..models import ContaNivel4


@admin.register(ContaNivel4)
class ContaNivel4Admin(BaseNovadataAdmin):
    list_display = [
        "id",
        "nome",
        "conta_nivel3",
    ]

    search_fields = [
        "id",
        "nome",
        "conta_nivel3__nome",
    ]

    list_filter = [
        ("conta_nivel3", RelatedOnlyDropdownFilter),
    ]

    autocomplete_fields = [
        "conta_nivel3",
    ]

    list_select_related = [
        "conta_nivel3",
    ]
