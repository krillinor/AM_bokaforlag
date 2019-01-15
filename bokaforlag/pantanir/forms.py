from django.forms import ModelForm, Textarea, Select
from .models import Pontun

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout


class PontunBokaknippiForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PontunBokaknippiForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.helper.layout = Layout(
            Div(
                Div("nafn", css_class="col-md-6"),
                Div("netfang", css_class="col-md-6"),
                css_class="row"
            ),
            Div(
                Div("kennitala", css_class="col-md-6"),
                Div("simanumer", css_class="col-md-6"),
                css_class="row"
            ),
            Div(
                Div("heimilisfang", css_class="col-md-6"),
                Div("postnumer", css_class="col-md-6"),
                css_class="row"
            ),
            Div(
                Div("stadur", css_class="col-md-6"),
                Div("land", css_class="col-md-6"),
                css_class="row"
            ),
            Div(
                Div("athugasemd", css_class="col-md-6"),
                Div("magn", css_class="col-md-6"),
                css_class="row"
            ),
        )

    class Meta:
        model = Pontun
        exclude = [
            "buin_til",
            "uppfaerd",
            "stada",
            "bok",
            "verd",
        ]
        MAGN_CHOICES = (
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
                ('5', '5'),
                )
        widgets = {
          "athugasemd": Textarea(attrs={'rows': 4}),
          'magn': Select(choices=MAGN_CHOICES, attrs={'cols': 1}),
        }
