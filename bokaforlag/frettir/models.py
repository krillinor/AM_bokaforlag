from django.db import models

def frettamynd_path(instance, filename):
    return f"frettamynd_{instance.titill}.{filename.split('.')[-1]}"

class Frett(models.Model):
    titill = models.CharField("Titill", max_length=128, blank=True, null=True)
    texti = models.TextField("Texti", max_length=2000, blank=False)
    tengill = models.URLField("Tengill", max_length=128, blank=True, null=True)
    tengill_texti = models.CharField("Texti á tengli", max_length=128, blank=True, null=True)
    mynd = models.ImageField(upload_to=frettamynd_path, blank=True)

    class Meta:
        ordering = ("id",)
        verbose_name = "Frétt"
        verbose_name_plural = "Fréttir"

    def __str__(self):
        return self.titill
