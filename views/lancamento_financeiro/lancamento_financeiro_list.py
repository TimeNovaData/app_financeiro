from datetime import datetime

from django.db.models import Q

from core.views import AcessoGeralView, BaseListView
from financeiro.forms import FiltroLancamentoFinanceiroForm
from financeiro.models import LancamentoFinanceiro
from global_functions.breadcrumb import make_breadcrumb
from global_functions.breadcrumb.itens import financeiro, lancamentos


class LancamentoFinanceiroListView(AcessoGeralView, BaseListView):
    model = LancamentoFinanceiro

    template_name = (
        "financeiro/lancamento_financeiro/lancamento_financeiro_list.html"
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["tipo"] = self.get_tipo()

        context["filtro_form"] = FiltroLancamentoFinanceiroForm(
            self.request.GET,
        )

        return context

    def get_simple_fields_filter(self):
        return [
            "id",
            "empresa__nome",
            "conta_gerencial__nome",
            "tipo_documento__nome",
        ]

    def get_columns(self):
        return {
            "id": "N° do lançamento",
            "compra__id": "Compra",
            "empresa__nome": "Empresa",
            "conta_gerencial__nome": "Conta gerencial",
            "destinacao": "Destinação",
            "tipo_documento__nome": "Documento",
            "valor_total": "Valor total",
            "previsao_pagamento": "Previsão de pagamento",
            "data_vencimento": "Data de vencimento",
        }

    def get_tipo(self):
        return self.request.GET.get("tipo", "Despesa")

    def get_queryset(self):
        query = super().get_queryset()

        query = query.filter(
            self.make_query_filter(),
            tipo=self.get_tipo(),
        )

        lancamentos_provisionados = self.request.GET.get(
            "lancamentos_provisionados", None
        )
        if lancamentos_provisionados:
            query = list(
                filter(
                    lambda objeto: objeto.data_vencimento
                    and (objeto.data_vencimento >= datetime.today().date()),
                    query,
                )
            )

        lancamentos_vencidos = self.request.GET.get(
            "lancamentos_vencidos", None
        )
        if lancamentos_vencidos:
            query = list(
                filter(
                    lambda objeto: objeto.data_vencimento
                    and (objeto.data_vencimento <= datetime.today().date())
                    and not objeto.pago,
                    query,
                )
            )

        lancamentos_pagos = self.request.GET.get("lancamentos_pagos", None)
        if lancamentos_pagos:
            query = list(filter(lambda objeto: objeto.pago, query))

        return query

    def make_query_filter(self):
        query = Q()

        data_inicial = self.request.GET.get("data_inicial", None)
        if data_inicial:
            query &= Q(data_criacao__gte=data_inicial)

        data_final = self.request.GET.get("data_final", None)
        if data_final:
            query &= Q(data_criacao__lte=data_final)

        empresa = self.request.GET.get("empresa", None)
        if empresa:
            query &= Q(empresa=empresa)

        return query

    def get_breadcrumb(self):
        return make_breadcrumb([financeiro, lancamentos])
