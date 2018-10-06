from django.contrib.auth.models import AbstractUser
import django.db.models as models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    email = models.EmailField(unique = True)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    # TODO nota regex
    # kennitala = models.
    heimilisfang = models.CharField(max_length=255)
    dags = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Notandi"
        verbose_name_plural = "Notendur"

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
