from django import forms

from global_functions.utils.forms import (
    prepare_form_fields,
    prepare_form_initial,
)

from ..models import CaixaBanco


class CaixaBancoForm(forms.ModelForm):
    class Meta:
        model = CaixaBanco

        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CaixaBancoForm, self).__init__(*args, **kwargs)
        self.fields = prepare_form_fields(self.fields)
        self.initial = prepare_form_initial(self.initial)
