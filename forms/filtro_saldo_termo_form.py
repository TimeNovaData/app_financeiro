from contratos.models import (
    Empresa,
    SituacaoTermoCooperacao,
    TermoCooperacaoNivel4,
)
from crum import get_current_user
from django import forms
from global_functions.utils.forms import prepare_form_fields


class FiltroSaldoTermoForm(forms.Form):
    empresa = forms.ModelChoiceField(
        label="Empresa",
        queryset=Empresa.objects.only_has_termo_cooperacao(),
        required=False,
    )

    ano_termo = forms.ChoiceField(
        label="Ano do termo",
        required=False,
        choices=[(None, "--------")],
    )

    situacao = forms.ModelChoiceField(
        label="Situação",
        queryset=SituacaoTermoCooperacao.objects.all(),
        required=False,
    )

    saldo_negativo_total = forms.BooleanField(
        label="Saldo negativo total",
        required=False,
    )

    saldo_positivo_total = forms.BooleanField(
        label="Saldo positivo total",
        required=False,
    )

    saldo_negativo_ppt = forms.BooleanField(
        label="Saldo negativo PPT",
        required=False,
    )

    saldo_negativo_capacitacao = forms.BooleanField(
        label="Saldo negativo capacitação",
        required=False,
    )

    saldo_negativo_divulgacao = forms.BooleanField(
        label="Saldo negativo divulgação",
        required=False,
    )

    saldo_negativo_equipamentos = forms.BooleanField(
        label="Saldo negativo equipamentos",
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(FiltroSaldoTermoForm, self).__init__(*args, **kwargs)
        self.fields = prepare_form_fields(self.fields)

        usuario = get_current_user()
        empresas = self.fields["empresa"].queryset.filter(
            usuarios_com_acesso=usuario
        )
        self.fields["empresa"].queryset = empresas

        anos_termos = (
            TermoCooperacaoNivel4.objects.filter(
                empresa__in=empresas,
                inicio_termo__isnull=False,
                fim_termo__isnull=False,
            )
            .distinct()
            .values_list(
                "inicio_termo",
                "fim_termo",
            )
        )

        for inicio_termo, fim_termo in list(set(anos_termos)):
            option = f"{inicio_termo.year} - {fim_termo.year}"
            choice = [(option, option)]
            self.fields["ano_termo"].choices += choice
