from django.views.generic import CreateView

from core.views import AcessoGeralView
from global_functions.breadcrumb import make_breadcrumb
from global_functions.breadcrumb.itens import (
    cadastros,
    financeiro,
    tipos_documentos_financeiros,
)

from ...forms import TipoDocumentoFinanceiroForm
from ...models import TipoDocumentoFinanceiro


class TipoDocumentoFinanceiroCreateView(AcessoGeralView, CreateView):
    model = TipoDocumentoFinanceiro

    form_class = TipoDocumentoFinanceiroForm

    template_name = "financeiro/tipo_documento_financeiro/tipo_documento_financeiro_form.html"

    def get_success_url(self):
        from global_functions.redirect import reverse_lazy_plus

        message = "Tipo de documento adicionado com sucesso!"
        return reverse_lazy_plus(
            "tipo_documento_financeiro_list",
            get_params={
                "mensagem_toastify": message,
            },
            just_uri=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Novo tipo de documento financeiro"

        return context

    def get_breadcrumb(self):
        novo_tipo_documento_financeiro = {
            "name": "Novo tipo de documento financeiro",
            "slug": "novo_tipo_documento_financeiro",
            "url_name": "tipo_documento_financeiro_create",
        }
        return make_breadcrumb(
            [
                financeiro,
                cadastros,
                tipos_documentos_financeiros,
                novo_tipo_documento_financeiro,
            ]
        )
