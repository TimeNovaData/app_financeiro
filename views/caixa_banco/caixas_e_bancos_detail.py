from django.views.generic import DetailView

from core.views import AcessoGeralView

from ...models import CaixaBanco


class CaixaBancoDetail(AcessoGeralView, DetailView):
    model = CaixaBanco

    template_name = (
        "financeiro/caixa_banco/caixas_bancos_detail/caixas_bancos_detail.html"
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Detalhes de caixas e bancos"

        return context

    def get_breadcrumb(view):
        from global_functions.breadcrumb import make_breadcrumb
        from global_functions.breadcrumb.itens import (
            caixas_bancos,
            financeiro,
            make_detalhes,
        )

        detalhes = make_detalhes(
            "caixas_e_bancos_detail",
            [view.object.id],
        )

        return make_breadcrumb([financeiro, caixas_bancos, detalhes])
