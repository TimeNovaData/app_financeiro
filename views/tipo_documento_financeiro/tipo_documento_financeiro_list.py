from core.views import AcessoGeralView, BaseListView
from global_functions.breadcrumb import make_breadcrumb
from global_functions.breadcrumb.itens import (
    cadastros,
    financeiro,
    tipos_documentos_financeiros,
)

from ...models import TipoDocumentoFinanceiro


class TipoDocumentoFinanceiroListView(AcessoGeralView, BaseListView):
    model = TipoDocumentoFinanceiro

    template_name = "financeiro/tipo_documento_financeiro/tipo_documento_financeiro_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Tipos de documento financeiro"

        return context

    def get_simple_fields_filter(self):
        return [
            "codigo",
            "nome",
        ]

    def get_breadcrumb(self):
        return make_breadcrumb(
            [
                financeiro,
                cadastros,
                tipos_documentos_financeiros,
            ]
        )
