from django.forms.models import inlineformset_factory

from ..models import LancamentoFinanceiro, Parcela
from .parcela_form import ParcelaForm

ParcelaInlineFormSet = inlineformset_factory(
    parent_model=LancamentoFinanceiro,
    model=Parcela,
    extra=0,
    form=ParcelaForm,
)
