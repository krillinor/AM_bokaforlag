import os
from unidecode import unidecode

from django.db import models
from django.utils.text import slugify


def mynd_path(instance, filename):
    filename, file_extension = os.path.splitext(filename)
    titill = instance.titill
    titill_slug = slugify(unidecode(titill))
    return f"mynd_{titill_slug}{file_extension}"


# TODO breyta þannig að mynd vísi á bók?
class Mynd(models.Model):
    titill = models.CharField(max_length=128)
    mynd = models.ImageField(upload_to=mynd_path, blank=False)

    class Meta:
        ordering = ("id",)
        verbose_name = "Mynd"
        verbose_name_plural = "Myndir"

    def __str__(self):
        return self.titill
