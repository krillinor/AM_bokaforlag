from django.db import models


def mynd_path(instance, filename):
    return f"myndalmenn_{instance.titill}.{filename.split('.')[-1]}"


class Mynd(models.Model):
    titill = models.CharField(max_length=128)
    mynd = models.ImageField(upload_to=mynd_path, blank=False)

    class Meta:
        ordering = ("id",)
        verbose_name = "Mynd"
        verbose_name_plural = "Myndir"

    def __str__(self):
        return self.titill
