from django import forms

class PantaBaekur(forms.Form):
    magn = forms.IntegerField(min_value=1, max_value=99)
