from django.urls import path

from .views import (
    baekur_lysing,
    bokaknippi,
)

app_name = "baekur"

urlpatterns = [
    path("<int:pk>", baekur_lysing, name="baekur_lysing"),
    path("bokaknippi", bokaknippi, name="bokaknippi"),
]
