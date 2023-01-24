from django.forms.models import inlineformset_factory

from ..models import ItemRateio, Rateio
from .item_rateio_form import ItemRateioForm

ItemRateioInlineFormSet = inlineformset_factory(
    parent_model=Rateio,
    model=ItemRateio,
    extra=0,
    min_num=1,
    form=ItemRateioForm,
)
