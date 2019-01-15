from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    RegexValidator
)
from ..baekur.models import Bok


# NB TODO field fyrir reikningsnúmer?
# TODO nota error_messages og help_text möguleika
class Pontun(models.Model):
    STADA = (
        ("EKKI_AFGREIDD", "Ekki afgreidd"),
        ("INNHEIMTA_SEND", "Innheimta send í heimabanka"),
        ("AFGREIDD", "Afgreidd"),
    )

    buin_til = models.DateTimeField(
        "Búin til",
        auto_now_add=True
    )
    uppfaerd = models.DateTimeField(
        "Uppfærð",
        auto_now=True
    )
    stada = models.CharField(
        "Staða",
        max_length=255,
        default="EKKI_AFGREIDD",
        choices=STADA
    )
    nafn = models.CharField(
        "Nafn",
        max_length=255
    )
    netfang = models.EmailField(
        "Netfang"
    )
    kennitala = models.CharField(
        "Kennitala",
        max_length=255,
        validators=[RegexValidator("^\d{6}-\d{4}$")],
        help_text="Skrifaðu kennitöluna á forminu XXXXXX-XXXX."
    )
    heimilisfang = models.CharField(
        "Heimilisfang",
        max_length=255
    )
    postnumer = models.CharField(
        "Póstnúmer",
        max_length=255
    )
    stadur = models.CharField(
        "Staður",
        max_length=255
    )
    land = models.CharField(
        "Land",
        max_length=255
    )
    # TODO phonenumberfield?
    simanumer = models.CharField(
        "Símanúmer",
        max_length=255
    )
    athugasemd = models.TextField("Athugasemd", blank=True)
    bok = models.ForeignKey(
        Bok,
        related_name="pantanir",
        verbose_name="Bók",
        on_delete=models.PROTECT,
        null=True
    )
    magn = models.PositiveIntegerField(
        "Fjöldi bókaknippa",
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(99),
        ]
        # help_text="Eitt bókaknippi samanstendur af fimm bókum."
    )
    verd = models.PositiveIntegerField(
        "Verð",
        null=True
    )

    class Meta:
        ordering = ("-buin_til",)
        verbose_name = "Pöntun"
        verbose_name_plural = "Pantanir"

    def __str__(self):
        return (f"Nafn: {self.nafn}. "
                f"Fjöldi bóka: {self.magn}.")

    def __repr__(self):
        return (f"Pöntun #{self.id} - "
                f"nafn: {self.nafn}")
