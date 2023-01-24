from core.views import AcessoGeralView, BaseListView
from django.db.models import Sum
from global_functions.breadcrumb import make_breadcrumb
from global_functions.breadcrumb.itens import financeiro, rateios

from ...models import Rateio


class RateioListView(AcessoGeralView, BaseListView):
    model = Rateio
    template_name = "financeiro/rateio/rateio_list.html"

    def get_totalizadores(self, **kwargs):
        totalizadores = super().get_totalizadores(**kwargs)

        valor_total = (
            self.get_queryset().aggregate(valor_total=Sum("valor"))[
                "valor_total"
            ]
            or 0
        )
        totalizadores["Valor total"] = round(valor_total, 2)

        return totalizadores

    def get_simple_fields_filter(self):
        return [
            "nome",
            "valor",
        ]

    def get_breadcrumb(self):
        return make_breadcrumb([financeiro, rateios])
