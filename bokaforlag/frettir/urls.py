from django.urls import path

from .views import frettir_view

app_name = "frettir"
urlpatterns = [
    path("", frettir_view, name="frettir"),
]
