from django.views.generic import DetailView

from core.views import AcessoGeralView
from global_functions.breadcrumb import make_breadcrumb
from global_functions.breadcrumb.itens import (
    financeiro,
    lancamentos,
    make_detalhes,
)

from ...models import LancamentoFinanceiro


class LancamentoFinanceiroDetailView(AcessoGeralView, DetailView):
    model = LancamentoFinanceiro

    template_name = "financeiro/lancamento_financeiro/lancamento_financeiro_detail/lancamento_financeiro_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["tipo"] = self.get_tipo()
        return context

    def get_tipo(self):
        return self.request.GET.get("tipo", "Despesa")

    def get_breadcrumb(view):
        lancamentos["get_params"] = {
            "tipo": view.get_tipo(),
        }

        detalhes = make_detalhes(
            "lancamento_financeiro_detail",
            url_params=[view.object.pk],
            get_params={
                "tipo": view.get_tipo(),
            },
        )
        return make_breadcrumb([financeiro, lancamentos, detalhes])
