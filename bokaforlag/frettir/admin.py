from django.contrib import admin
from .models import Frett

@admin.register(Frett)
class FrettAdmin(admin.ModelAdmin):
    list_display = (
        "titill",
        "texti",
        "tengill",
        "tengill_texti",
    )
