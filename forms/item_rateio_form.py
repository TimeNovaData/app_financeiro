from django import forms
from global_functions.utils.forms import prepare_form_fields

from ..models import ItemRateio


class ItemRateioForm(forms.ModelForm):
    class Meta:
        model = ItemRateio

        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ItemRateioForm, self).__init__(*args, **kwargs)
        self.fields = prepare_form_fields(self.fields)
        self.fields["porcentagem"].widget.attrs["max"] = 100
        self.fields["porcentagem"].widget.attrs["required"] = True
