from django import forms

from global_functions.utils.forms import (
    prepare_form_fields,
    prepare_form_initial,
)

from ..models import Parcela


class ParcelaForm(forms.ModelForm):
    class Meta:
        model = Parcela

        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ParcelaForm, self).__init__(*args, **kwargs)
        self.fields = prepare_form_fields(self.fields)
        self.initial = prepare_form_initial(self.initial)
        self.fields["valor"].widget.attrs["min"] = 0
