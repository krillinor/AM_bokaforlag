from django.db import models
from markdownx.models import MarkdownxField
from django.db.models import F



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
    titill = models.CharField(
        "Bókartitill",
        max_length=255
        # unique=True
    )
    hofundur = models.ManyToManyField(
        Hofundur,
        related_name="baekur",
        verbose_name="Höfundur"
    )
    stutt_lysing = models.TextField("Stutt lýsing", blank=True)
    long_lysing = models.TextField(
        "Löng lýsing",
        help_text="Notaðu Markdown til að skrifa lýsinguna: https://en.wikipedia.org/wiki/Markdown. Tvö bil til að skipta yfir í næstu línu."
    )
    verd = models.PositiveIntegerField("Verð")
    syna_verd = models.BooleanField("Sýna verð", default=True)
    # TODO bæta við að geti verið >1?
    mynd = models.ImageField(upload_to=bokarmynd_path, blank=True)

    class Meta:
        ordering = ("titill",)
        verbose_name = "Bók"
        verbose_name_plural = "Bækur"

    def __str__(self):
        return self.titill

    def save(self, *args, **kwargs):
        try:
            pantanir = self.pantanir.all()
            pantanir.update(verd = self.verd * F("magn"))
            pantanir.save()
        # ?
        except Exception as e:
            print(e)
        super(Bok, self).save(*args, **kwargs)
