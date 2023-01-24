from django import forms

from global_functions.utils.forms import prepare_form_fields

from ..models import ContaNivel1


class ContaNivel1Form(forms.ModelForm):
    class Meta:
        model = ContaNivel1

        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ContaNivel1Form, self).__init__(*args, **kwargs)
        self.fields = prepare_form_fields(self.fields)
