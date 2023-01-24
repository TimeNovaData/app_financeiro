from django import forms
from global_functions.utils.forms import prepare_form_fields


class FiltroParcelaForm(forms.Form):
    TIPO_CHOICES = [
        ("", "--------"),
        ("Receita", "Receita"),
        ("Despesa", "Despesa"),
    ]

    tipo = forms.ChoiceField(
        choices=TIPO_CHOICES,
        required=False,
    )

    data_inicial = forms.DateField(
        label="De:",
        required=False,
    )

    data_final = forms.DateField(
        label="Até:",
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(FiltroParcelaForm, self).__init__(*args, **kwargs)
        self.fields = prepare_form_fields(self.fields)
