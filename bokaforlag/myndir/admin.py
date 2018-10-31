from django.contrib import admin
from .models import Mynd

@admin.register(Mynd)
class MyndAdmin(admin.ModelAdmin):
    list_display = (
        "titill",
    )
