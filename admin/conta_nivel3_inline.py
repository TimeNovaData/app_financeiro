from django.contrib import admin

from ..models import ContaNivel3


class ContaNivel3Inline(admin.TabularInline):
    model = ContaNivel3

    extra = 0
