from django.contrib import admin
from .models import Pontun

import csv
import datetime

from django.http import HttpResponse
from django.utils.safestring import mark_safe

from django.urls import reverse



def ekki_afgreidd(modeladmin, request, queryset):
    queryset.update(stada="EKKI_AFGREIDD",
                    uppfaerd=datetime.datetime.now())
ekki_afgreidd.short_description = "Merkja sem „Ekki afgreidd“"

def innheimta_send(modeladmin, request, queryset):
    queryset.update(stada="INNHEIMTA_SEND",
                    uppfaerd=datetime.datetime.now())
innheimta_send.short_description = "Merkja sem „Innheimta send í heimabanka“"

def afgreidd(modeladmin, request, queryset):
    queryset.update(stada="AFGREIDD",
                    uppfaerd=datetime.datetime.now())
afgreidd.short_description = "Merkja sem „Afgreidd“"

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment;"\
    "filename={}.csv".format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [
        field for field in opts.get_fields() if not field.many_to_many\
        and not field.one_to_many
    ]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime("%d/%m/%Y")
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = "Skrifa sem csv-skrá"


@admin.register(Pontun)
class PontunAdmin(admin.ModelAdmin):
    list_display = (
        "pontun_lysing",
        "bok",
        "magn",
        "verd",
        "nafn",
        "litud_stada",
        "uppfaerd",
        "buin_til",
    )
    search_fields = ("nafn",)
    list_filter = ("stada",)
    actions = [
        ekki_afgreidd,
        innheimta_send,
        afgreidd,
        export_to_csv
    ]

    def pontun_lysing(self, obj):
        return mark_safe("<a href='{}'>Skoða</a>".format(
            reverse("admin_pontun_lysing", args=[obj.id]))
        )
    pontun_lysing.short_description = "Allar upplýsingar"

    def litud_stada(self, obj):
        if obj.stada == "EKKI_AFGREIDD":
            color = "red"
        elif obj.stada == "INNHEIMTA_SEND":
            color = "orange"
        else:
            color = "green"
        return mark_safe(f"<strong style='color: {color};'>{obj.get_stada_display()}</strong>")
    litud_stada.short_description = "Staða"
