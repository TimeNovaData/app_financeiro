from core.views import AcessoGeralView
from django.views.generic import DetailView
from financeiro.models import Rateio


class RateioDetailView(AcessoGeralView, DetailView):
    model = Rateio

    template_name = "financeiro/rateio/rateio_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Detalhes do rateio"

        return context

    def get_breadcrumb(self):
        from global_functions.breadcrumb import (
            crud_breadcrumbs,
            make_breadcrumb,
        )
        from global_functions.breadcrumb.itens import financeiro

        return make_breadcrumb(
            [
                financeiro,
                crud_breadcrumbs.list_breadcrumb(Rateio),
                crud_breadcrumbs.detail_breadcrumb(
                    Rateio, url_params=[self.get_object().id]
                ),
            ]
        )
