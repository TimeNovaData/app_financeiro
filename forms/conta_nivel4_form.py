from django import forms

from global_functions.utils.forms import prepare_form_fields

from ..models import ContaNivel4


class ContaNivel4Form(forms.ModelForm):
    class Meta:
        model = ContaNivel4

        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ContaNivel4Form, self).__init__(*args, **kwargs)
        self.fields = prepare_form_fields(self.fields)
