from django.urls import path

from .views import (
    baekur_lysing,
    bokaknippi
    # baekur_listi,
    # hofundar_listi,
    # hofundar_baekur,
)

app_name = "baekur"

urlpatterns = [
    path("<int:pk>", baekur_lysing, name="baekur_lysing"),
    path("bokaknippi", bokaknippi, name="bokaknippi"),
    # path("", baekur_listi, name="baekur_listi"),
    # path("hofundar", hofundar_listi, name="hofundar_listi"),
    # path("hofundar/<int:pk>", hofundar_baekur, name="hofundar_baekur"),
]
