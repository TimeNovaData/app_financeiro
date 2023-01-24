from django import forms

from ..models import TipoDocumentoFinanceiro
from global_functions.utils.forms import prepare_form_fields

class TipoDocumentoFinanceiroForm(forms.ModelForm):
    class Meta:
        model = TipoDocumentoFinanceiro
        
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TipoDocumentoFinanceiroForm, self).__init__(*args, **kwargs)
        self.fields = prepare_form_fields(self.fields)
