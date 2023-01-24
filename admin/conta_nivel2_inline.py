from django.contrib import admin

from ..models import ContaNivel2


class ContaNivel2Inline(admin.TabularInline):
    model = ContaNivel2

    extra = 0
