from django.db import models



class Hofundur(models.Model):
    fornafn = models.CharField("Fornafn", max_length=255)
    eftirnafn = models.CharField("Eftirnafn", max_length=255)

    class Meta:
        ordering = ("fornafn", "eftirnafn",)
        verbose_name = "Höfundur"
        verbose_name_plural = "Höfundar"

    def __str__(self):
        return self.fornafn + ' ' + self.eftirnafn


# TODO díla við margar myndir
def bokarmynd_path(instance, filename):
    return f"bok{instance.pk}.png"

class Bok(models.Model):
    titill = models.CharField("Bókartitill", max_length=255)
    hofundur = models.ManyToManyField(Hofundur, related_name="baekur")
    stutt_lysing = models.TextField("Stutt lýsing", blank=True)
    long_lysing = models.TextField("Löng lýsing")
    verd = models.PositiveIntegerField("Verð")
    # TODO ?
    mynd = models.ImageField(upload_to=bokarmynd_path, blank=True)

    class Meta:
        ordering = ("titill",)
        verbose_name = "Bók"
        verbose_name_plural = "Bækur"

    def __str__(self):
        return self.titill
