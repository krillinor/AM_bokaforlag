from datetime import datetime
import os
from unidecode import unidecode

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify


class Hofundur(models.Model):
    nafn = models.CharField("nafn", max_length=255)

    class Meta:
        ordering = ("nafn",)
        verbose_name = "Höfundur"
        verbose_name_plural = "Höfundar"

    def __str__(self):
        return self.nafn


def bokarmynd_path(instance, filename):
    filename, file_extension = os.path.splitext(filename)
    titill = instance.titill
    titill_slug = slugify(unidecode(titill))
    return f"bok_{titill_slug}{file_extension}"


class Bok(models.Model):
    titill = models.CharField(
        "Bókartitill",
        max_length=255
        # ?
        # unique=True
    )
    hofundur = models.ManyToManyField(
        Hofundur,
        related_name="baekur",
        verbose_name="Höfundur"
    )
    stutt_lysing = models.TextField(
        "Stutt lýsing",
        blank=True
    )
    long_lysing = models.TextField(
        "Löng lýsing",
        help_text="Notaðu Markdown til að skrifa lýsinguna: "
                  "https://en.wikipedia.org/wiki/Markdown. "
                  "Tvö bil til að skipta yfir í næstu línu."
    )
    verd = models.PositiveIntegerField(
        "Verð"
    )
    afslattur = models.PositiveIntegerField(
        "Afsláttur í kr.",
        default=0,
        blank=True
    )
    afsl_byrjar = models.DateField(
        "Afsláttur byrjar",
        null=True,
        blank=True
    )
    afsl_endar = models.DateField(
        "Afsláttur endar",
        null=True,
        blank=True
    )
    syna_verd = models.BooleanField(
        "Sýna verð",
        default=True
    )
    # TODO bæta við að geti verið >1?
    mynd = models.ImageField(
        "Mynd",
        upload_to=bokarmynd_path,
        blank=True
    )

    class Meta:
        ordering = ("titill",)
        verbose_name = "Bók"
        verbose_name_plural = "Bækur"

    def __str__(self):
        return self.titill

    def clean(self):
        if self.afslattur >= self.verd:
            raise ValidationError(
                "Afsláttur verður að vera minni en vöruverð."
            )

    def er_afslattur(self):
        if (
            self.afslattur > 0 and
            self.afsl_byrjar and
            self.afsl_endar
        ):
            if (
                self.afsl_byrjar
                <= datetime.now().date()
                <= self.afsl_endar
            ):
                return True
        return False

    @property
    def verd_m_afslaetti(self):
        if (
            self.afslattur > 0 and
            self.afsl_byrjar and
            self.afsl_endar
        ):
            if (
                self.afsl_byrjar
                <= datetime.now().date()
                <= self.afsl_endar
            ):
                nytt_verd = self.verd - self.afslattur
                return nytt_verd
        return self.verd
