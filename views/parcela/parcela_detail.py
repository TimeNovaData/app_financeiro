from django.views.generic import DetailView

from core.views import AcessoGeralView
from global_functions.breadcrumb import make_breadcrumb
from global_functions.breadcrumb.itens import (
    financeiro,
    make_detalhes,
    parcelas,
)

from ...models import Parcela


class ParcelaDetailView(AcessoGeralView, DetailView):
    model = Parcela

    template_name = "financeiro/parcela/parcela_detail/parcela_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_breadcrumb(view):
        detalhes = make_detalhes(
            "parcela_detail",
            url_params=[view.object.pk],
        )
        return make_breadcrumb([financeiro, parcelas, detalhes])
