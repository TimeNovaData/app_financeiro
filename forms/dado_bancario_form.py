from django import forms

from global_functions.utils.forms import prepare_form_fields

from ..models import DadoBancario


class DadoBancarioForm(forms.ModelForm):
    class Meta:
        model = DadoBancario

        fields = [
            "banco",
            "agencia",
            "conta",
        ]

    def __init__(self, *args, **kwargs):
        super(DadoBancarioForm, self).__init__(*args, **kwargs)
        self.fields = prepare_form_fields(self.fields)
