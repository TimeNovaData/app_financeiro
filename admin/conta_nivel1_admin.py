from core.admin import BaseNovadataAdmin
from django.contrib import admin

from ..models import ContaNivel1
from .conta_nivel2_inline import ContaNivel2Inline


@admin.register(ContaNivel1)
class ContaNivel1Admin(BaseNovadataAdmin):
    list_display = [
        "id",
        "nome",
    ]

    search_fields = [
        "id",
        "nome",
    ]

    inlines = [
        ContaNivel2Inline,
    ]
