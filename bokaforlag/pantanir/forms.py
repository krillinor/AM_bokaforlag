from django.forms import ModelForm, Textarea
from .models import Pontun

from ..baekur.models import Bok

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Field, Fieldset, ButtonHolder, Submit

from django.core.mail import send_mail




# NB bara gagnlegt til að panta bókaknippið - BREYTA SEINNA
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
                Div("magn", css_class="col-md-2"),
                css_class="row"
            )
        )
        #     # Field("heimilisfang", css_class="col-9"),
        #     # Field("postnumer", css_class="col-3"),
        #     # Field("stadur", css_class="col-6"),
        #     # Field("land", css_class="col-6"),
        #     # Field("athugasemd"),
        #     # Field("magn", css_class="col-6"),
        # )


    class Meta:
        model = Pontun
        exclude = [
            "buin_til",
            "uppfaerd",
            "stada",
            "bok",
            "verd",
        ]
        widgets = {
          "athugasemd": Textarea(attrs={'rows': 4}),
        }
