from core.views import AcessoGeralView, BaseListView
from global_functions.breadcrumb import make_breadcrumb
from global_functions.breadcrumb.itens import caixas_bancos, financeiro

from ...models import CaixaBanco


class CaixaBancoListView(AcessoGeralView, BaseListView):
    model = CaixaBanco
    template_name = "financeiro/caixa_banco/caixas_e_bancos_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_simple_fields_filter(self):
        return [
            "nome",
            "tipo_conta__nome",
            "periodo_abertura__nome",
            "periodo_encerramento__nome",
        ]

    def get_booleans_fields_filter(self):
        return [
            "considerar_fluxo_caixa",
        ]

    def get_breadcrumb(self):
        return make_breadcrumb([financeiro, caixas_bancos])
