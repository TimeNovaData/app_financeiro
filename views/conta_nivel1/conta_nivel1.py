from core.views import AcessoGeralView, BaseListView
from global_functions.breadcrumb import make_breadcrumb
from global_functions.breadcrumb.itens import (
    cadastros,
    financeiro,
    make_grupo_contas,
)

from ...models import ContaNivel1


class ContaNivel1ListView(AcessoGeralView, BaseListView):
    model = ContaNivel1
    template_name = "financeiro/conta_nivel1/conta_nivel1_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_simple_fields_filter(self):
        return [
            "nome",
        ]

    def get_breadcrumb(self):
        grupo_contas = make_grupo_contas("conta_nivel1")
        return make_breadcrumb([financeiro, cadastros, grupo_contas])
