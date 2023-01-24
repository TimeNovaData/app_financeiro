from core.views import AcessoGeralView, BaseListView
from global_functions.breadcrumb import make_breadcrumb
from global_functions.breadcrumb.itens import (
    cadastros,
    financeiro,
    make_grupo_contas,
)

from ...models import ContaNivel3


class ContaNivel3ListView(AcessoGeralView, BaseListView):
    model = ContaNivel3
    template_name = "financeiro/conta_nivel3/conta_nivel3_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_simple_fields_filter(self):
        return [
            "conta_nivel2__conta_nivel1__nome",
            "conta_nivel2__nome",
            "nome",
        ]

    def get_breadcrumb(self):
        grupo_contas = make_grupo_contas("conta_nivel3")
        return make_breadcrumb([financeiro, cadastros, grupo_contas])
