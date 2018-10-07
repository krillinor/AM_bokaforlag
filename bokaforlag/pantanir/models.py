from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    RegexValidator
)


# TODO nota error_messages og help_text möguleika
class Pontun(models.Model):
    STADA = (
        ("EKKI_AFGREIDD", "Ekki afgreidd"),
        ("INNHEIMTA_SEND", "Innheimta send í heimabanka"),
        ("AFGREIDD", "Afgreidd"),
    )

    buin_til = models.DateTimeField("Búin til þann", auto_now_add=True)
    uppfaerd = models.DateTimeField("Uppfærð þann", auto_now=True)
    stada = models.CharField("Staða",
                             max_length=255,
                             default="EKKI_AFGREIDD",
                             choices=STADA)

    nafn = models.CharField("Nafn", max_length=255)
    netfang = models.EmailField("Netfang")
    kennitala = models.CharField(
        "Kennitala",
        max_length=255,
        validators=[
            RegexValidator("^\d{10}$")
        ]
    )
    heimilisfang = models.CharField("Heimilisfang", max_length=255)
    postnumer = models.CharField("Póstnúmer", max_length=255)
    stadur = models.CharField("Staður", max_length=255)
    land = models.CharField("Land", max_length=255)
    # TODO phonenumberfield?
    simanumer = models.CharField(
        "Símanúmer",
        max_length=255,
        validators=[
            RegexValidator("^\d+$")
        ]
    )
    athugasemd = models.TextField("Athugasemd", blank=True)
    # TODO hef engar orderlines núna því bara ein vara - breyta seinna
    bok = models.CharField("Bók", max_length=255)
    magn = models.PositiveIntegerField(
        "Magn",
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(99),
        ]
    )

    class Meta:
        ordering = ("-buin_til",)
        verbose_name = "Pöntun"
        verbose_name_plural = "Pantanir"

    def __str__(self):
        return (f"Nafn: {self.nafn}. "
                f"Fjöldi bóka: {self.magn}.")
