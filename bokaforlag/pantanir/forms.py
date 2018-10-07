from django.forms import ModelForm
from .models import Pontun



class PontunForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.bok = kwargs.pop("bok")
        super(PontunForm, self).__init__(*args, **kwargs)
        self.instance.bok = self.bok

    class Meta:
        model = Pontun
        exclude = [
            "buin_til",
            "uppfaerd",
            "stada",
            "bok",
        ]
