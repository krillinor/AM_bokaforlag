from django.contrib import admin

from .models import Hofundur, Bok


@admin.register(Bok)
class BokAdmin(admin.ModelAdmin):
    list_display = (
        "titill",
        "hofundar",
        "verd",
    )

    def hofundar(self, obj):
        return ", ".join([h.nafn for h in obj.hofundur.all()])

admin.site.register(Hofundur)
