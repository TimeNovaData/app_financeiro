from core.views import AcessoGeralView, BaseListView
from global_functions.breadcrumb import make_breadcrumb
from global_functions.breadcrumb.itens import (
    cadastros,
    financeiro,
    make_grupo_contas,
)

from ...models import ContaNivel4


class ContaNivel4ListView(AcessoGeralView, BaseListView):
    model = ContaNivel4
    template_name = "financeiro/conta_nivel4/conta_nivel4_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_simple_fields_filter(self):
        return [
            "conta_nivel3__conta_nivel2__conta_nivel1__nome",
            "conta_nivel3__conta_nivel2__nome",
            "conta_nivel3__nome",
            "nome",
        ]

    def get_breadcrumb(self):
        grupo_contas = make_grupo_contas("conta_nivel4")
        return make_breadcrumb([financeiro, cadastros, grupo_contas])
