from core.views import AcessoGeralView, BaseListView
from global_functions.breadcrumb import make_breadcrumb
from global_functions.breadcrumb.itens import (
    cadastros,
    financeiro,
    make_grupo_contas,
)

from ...models import ContaNivel2


class ContaNivel2ListView(AcessoGeralView, BaseListView):
    model = ContaNivel2
    template_name = "financeiro/conta_nivel2/conta_nivel2_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_simple_fields_filter(self):
        return [
            "conta_nivel1__nome",
            "nome",
        ]

    def get_breadcrumb(self):
        grupo_contas = make_grupo_contas("conta_nivel2")
        return make_breadcrumb([financeiro, cadastros, grupo_contas])
