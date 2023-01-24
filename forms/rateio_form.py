from django import forms

from global_functions.utils.forms import prepare_form_fields

from ..models import Rateio


class RateioForm(forms.ModelForm):
    class Meta:
        model = Rateio

        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(RateioForm, self).__init__(*args, **kwargs)
        self.fields = prepare_form_fields(self.fields)
        self.fields["conta_caixa"].queryset = self.fields[
            "conta_caixa"
        ].queryset.filter(aceita_lancamentos=True)
