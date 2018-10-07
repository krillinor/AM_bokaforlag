from django.contrib import admin
from .models import Pontun

import datetime


def innheimta_send(modeladmin, request, queryset):
    queryset.update(stada="INNHEIMTA_SEND",
                    uppfaerd=datetime.datetime.now())
innheimta_send.short_description = "Merkja sem „Innheimta send í heimabanka“"

def afgreidd(modeladmin, request, queryset):
    queryset.update(stada="AFGREIDD",
                    uppfaerd=datetime.datetime.now())
afgreidd.short_description = "Merkja sem „Afgreidd“"


@admin.register(Pontun)
class PontunAdmin(admin.ModelAdmin):
    list_display = (
        "nafn",
        "bok",
        "magn",
        "stada",
        "uppfaerd",
        "buin_til",
    )
    search_fields = ("nafn",)
    list_filter = ("stada",)
    actions = [
        innheimta_send,
        afgreidd,
    ]
