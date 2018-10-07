from django.urls import path

from bokaforlag.baekur.views import (
    baekur_listi,
    baekur_lysing,
    hofundar_listi,
    hofundar_baekur,
    baekur_forsida
)

app_name = "baekur"
urlpatterns = [
    path("", baekur_listi, name="baekur_listi"),
    path("<int:pk>", baekur_lysing, name="baekur_lysing"),
    path("hofundar", hofundar_listi, name="hofundar_listi"),
    path("hofundar/<int:pk>", hofundar_baekur, name="hofundar_baekur"),
]
