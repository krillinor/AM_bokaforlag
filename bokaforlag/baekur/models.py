from django.db import models



class Hofundur(models.Model):
    nafn = models.CharField("nafn", max_length=255)

    class Meta:
        ordering = ("nafn",)
        verbose_name = "Höfundur"
        verbose_name_plural = "Höfundar"

    def __str__(self):
        return self.nafn


# NB TODO finna betri lausn
# TODO díla við margar myndir
def bokarmynd_path(instance, filename):
    return f"mynd_{instance.titill}"

class Bok(models.Model):
    titill = models.CharField("Bókartitill", max_length=255)
    hofundur = models.ManyToManyField(Hofundur, related_name="baekur")
    stutt_lysing = models.TextField("Stutt lýsing", blank=True)
    long_lysing = models.TextField("Löng lýsing")
    verd = models.PositiveIntegerField("Verð")
    # TODO bæta við að geti verið >1?
    mynd = models.ImageField(upload_to=bokarmynd_path, blank=True)

    class Meta:
        ordering = ("titill",)
        verbose_name = "Bók"
        verbose_name_plural = "Bækur"

    def __str__(self):
        return self.titill
