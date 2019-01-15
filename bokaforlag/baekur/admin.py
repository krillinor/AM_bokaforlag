from django.contrib import admin

from .models import Hofundur, Bok


@admin.register(Bok)
class BokAdmin(admin.ModelAdmin):
    list_display = (
        "titill",
        "na_i_hofunda",
        "verd",
        "afslattur"
    )

    def na_i_hofunda(self, obj):
        return ", ".join([h.nafn for h in obj.hofundur.all()])
    na_i_hofunda.short_description = "Höfundur"


@admin.register(Hofundur)
class Hofundur(admin.ModelAdmin):
    list_display = (
        "nafn",
        "na_i_baekur",
    )

    def na_i_baekur(self, obj):
        return ", ".join([b.titill for b in obj.baekur.all()])
    na_i_baekur.short_description = "Bækur"
