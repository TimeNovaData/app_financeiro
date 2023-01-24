from django.contrib import admin

from ..models import DadoBancario


class DadoBancarioInline(admin.StackedInline):
    model = DadoBancario

    extra = 0

    min_num = 1

    autocomplete_fields = [
        'banco',
    ]

    fields = [
        'banco',
        'agencia',
        'conta',
    ]
