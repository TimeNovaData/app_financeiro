from datetime import datetime

from django import forms
from financeiro.models import Parcela
from global_functions.utils.forms import (
    prepare_form_fields,
    prepare_form_initial,
)


class PagarParcelaForm(forms.ModelForm):
    class Meta:
        model = Parcela
        fields = [
            "caixa_banco_real",
            "conta_gerencial",
            "observacoes",
            "data_pagamento",
        ]

    def __init__(self, *args, **kwargs):
        super(PagarParcelaForm, self).__init__(*args, **kwargs)
        self.fields = prepare_form_fields(self.fields)
        self.initial = prepare_form_initial(self.initial)
        self.fields["data_pagamento"].initial = datetime.today().strftime(
            "%Y-%m-%d"
        )
