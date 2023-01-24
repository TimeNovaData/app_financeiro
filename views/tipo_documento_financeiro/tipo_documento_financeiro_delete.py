
from django.views.generic import DeleteView

from core.views import AcessoGeralView
from global_functions.breadcrumb import make_breadcrumb
from global_functions.breadcrumb.itens import (cadastros, financeiro,
                                               tipos_documentos_financeiros)

from ...models import TipoDocumentoFinanceiro


class TipoDocumentoFinanceiroDeleteView(AcessoGeralView, DeleteView):
    model = TipoDocumentoFinanceiro

    def get_success_url(self):
        from global_functions.redirect import reverse_lazy_plus

        return reverse_lazy_plus(
            "tipo_documento_financeiro_list",
            get_params={
                "mensagem_toastify": "Tipo de documento removido com sucesso!",
                "tipo": self.object.tipo,
            },
            just_uri=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Excluir tipo de documento financeiro"

        return context

    def get_breadcrumb(self):
        excluir_tipo_documento_financeiro = {
            "name": "Excluir tipo de documento financeiro",
            "slug": "excluir_tipo_documento_financeiro",
            "url_name": "",
        }
        return make_breadcrumb(
            [
                financeiro,
                cadastros,
                tipos_documentos_financeiros,
                excluir_tipo_documento_financeiro,
            ]
        )
