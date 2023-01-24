from django.contrib import admin

from ..models import ContaNivel1


class ContaNivel1Inline(admin.TabularInline):
    model = ContaNivel1

    extra = 0
