from contratos.models import (
    TermoCooperacaoNivel1,
    TermoCooperacaoNivel2,
    TermoCooperacaoNivel3,
    TermoCooperacaoNivel4,
)
from django import forms
from financeiro.models import (
    ContaNivel1,
    ContaNivel2,
    ContaNivel3,
    ContaNivel4,
)
from global_functions.utils.forms import prepare_form_fields


class FiltroFluxoCaixaForm(forms.Form):
    TIPO_PERIODO_CHOICES = (
        (None, "---------"),
        ("Diário", "Diário"),
        ("Mensal", "Mensal"),
        ("Anual", "Anual"),
    )

    tipo_periodo = forms.ChoiceField(
        choices=TIPO_PERIODO_CHOICES,
        required=False,
        label="Tipo de período",
    )

    data_inicial = forms.DateField(
        required=False,
        label="De:",
    )

    data_final = forms.DateField(
        required=False,
        label="Até:",
    )

    projetos_nivel1 = forms.ModelChoiceField(
        queryset=TermoCooperacaoNivel1.objects.all(),
        required=False,
        label="Projets de nível 1",
    )

    projetos_nivel2 = forms.ModelChoiceField(
        queryset=TermoCooperacaoNivel2.objects.all(),
        required=False,
        label="Projets de nível 2",
    )

    projetos_nivel3 = forms.ModelChoiceField(
        queryset=TermoCooperacaoNivel3.objects.all(),
        required=False,
        label="Projets de nível 3",
    )

    projetos_nivel4 = forms.ModelChoiceField(
        queryset=TermoCooperacaoNivel4.objects.all(),
        required=False,
        label="Projets de nível 4",
    )

    contas_nivel1 = forms.ModelChoiceField(
        queryset=ContaNivel1.objects.all(),
        required=False,
        label="Contas de nível 1",
    )

    contas_nivel2 = forms.ModelChoiceField(
        queryset=ContaNivel2.objects.all(),
        required=False,
        label="Contas de nível 2",
    )

    contas_nivel3 = forms.ModelChoiceField(
        queryset=ContaNivel3.objects.all(),
        required=False,
        label="Contas de nível 3",
    )

    contas_nivel4 = forms.ModelChoiceField(
        queryset=ContaNivel4.objects.all(),
        required=False,
        label="Contas de nível 4",
    )

    somente_provisionadas = forms.BooleanField(
        required=False,
        label="Somente provisionadas",
    )

    def __init__(self, *args, **kwargs):
        super(FiltroFluxoCaixaForm, self).__init__(*args, **kwargs)
        self.fields = prepare_form_fields(self.fields)
