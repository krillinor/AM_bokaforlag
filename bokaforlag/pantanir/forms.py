from django.forms import ModelForm
from .models import Pontun

from ..baekur.models import Bok



# NB bara gagnlegt til að panta bókaknippið - BREYTA SEINNA
class PontunBokaknippiForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     self.bok = kwargs.pop("bok")
    #     super(PontunBokaknippiForm, self).__init__(*args, **kwargs)
    #     self.instance.bok = self.bok

    class Meta:
        model = Pontun
        exclude = [
            "buin_til",
            "uppfaerd",
            "stada",
            "bok",
            "verd",
        ]
