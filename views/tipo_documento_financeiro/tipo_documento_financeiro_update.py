from django.views.generic import UpdateView

from core.views import AcessoGeralView
from global_functions.breadcrumb import make_breadcrumb
from global_functions.breadcrumb.itens import (
    cadastros,
    financeiro,
    tipos_documentos_financeiros,
)

from ...forms import TipoDocumentoFinanceiroForm
from ...models import TipoDocumentoFinanceiro


class TipoDocumentoFinanceiroUpdateView(AcessoGeralView, UpdateView):
    model = TipoDocumentoFinanceiro

    form_class = TipoDocumentoFinanceiroForm

    template_name = "financeiro/tipo_documento_financeiro/tipo_documento_financeiro_form.html"

    def get_success_url(self):
        from global_functions.redirect import reverse_lazy_plus

        return reverse_lazy_plus(
            "tipo_documento_financeiro_list",
            get_params={
                "mensagem_toastify": "Tipo de documento alterado com sucesso!",
            },
            just_uri=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar tipo de documento financeiro"

        return context

    def get_breadcrumb(self):
        editar_tipo_documento_financeiro = {
            "name": "Editar tipo de documento financeiro",
            "slug": "editar_tipo_documento_financeiro",
            "url_name": "",
        }
        return make_breadcrumb(
            [
                financeiro,
                cadastros,
                tipos_documentos_financeiros,
                editar_tipo_documento_financeiro,
            ]
        )
