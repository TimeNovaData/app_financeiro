from contratos.models import Empresa
from django import forms
from global_functions.utils.forms import prepare_form_fields


class FiltroLancamentoFinanceiroForm(forms.Form):
    empresa = forms.ModelChoiceField(
        label="Empresa",
        queryset=Empresa.objects.all(),
        required=False,
    )

    lancamentos_provisionados = forms.BooleanField(
        label="Lançamentos provisionados",
        required=False,
    )

    lancamentos_vencidos = forms.BooleanField(
        label="Lançamentos vencidos",
        required=False,
    )

    lancamentos_pagos = forms.BooleanField(
        label="Lançamentos pagos",
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
        super(FiltroLancamentoFinanceiroForm, self).__init__(*args, **kwargs)
        self.fields = prepare_form_fields(self.fields)
