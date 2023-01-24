from django import forms

from global_functions.utils.forms import prepare_form_fields

from ..models import ContaNivel3


class ContaNivel3Form(forms.ModelForm):
    class Meta:
        model = ContaNivel3

        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ContaNivel3Form, self).__init__(*args, **kwargs)
        self.fields = prepare_form_fields(self.fields)
