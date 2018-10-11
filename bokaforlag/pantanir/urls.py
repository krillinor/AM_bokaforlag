from django.urls import path

from .views import (
    panta_bokaknippi,
    pontun_tokst
)

app_name = "pantanir"
urlpatterns = [
    path("panta", panta_bokaknippi, name="panta_bokaknippi"),
    path("pontun_tokst", pontun_tokst, name="pontun_tokst"),
]
