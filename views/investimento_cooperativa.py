from contratos.models import Empresa
from core.views import AcessoGeralView, BaseListView
from global_functions.breadcrumb import make_breadcrumb
from global_functions.breadcrumb.itens import financeiro


class InvestimentoCooperativaListView(AcessoGeralView, BaseListView):
    model = Empresa

    template_name = "financeiro/investimento_cooperativa.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_queryset(self, **kwargs):
        query = super().get_queryset(**kwargs)
        return query.filter(is_cooperativa=True)

    def get_simple_fields_filter(self):
        return [
            "cnpj",
            "nome",
            "endereco__cidade",
            "endereco__estado",
        ]

    def get_totalizadores(self):
        totalizadores = super().get_totalizadores()

        valores_totais = [
            empresa.valor_total_termos for empresa in self.get_queryset()
        ]
        valores_totais_gastos = [
            empresa.valor_total_gasto for empresa in self.get_queryset()
        ]
        valores_totais_saldos = [
            empresa.valor_total_saldo for empresa in self.get_queryset()
        ]

        totalizadores["Valor total"] = sum(valores_totais)
        totalizadores["Total de gastos"] = sum(valores_totais_gastos)
        totalizadores["Total de saldos"] = sum(valores_totais_saldos)

        return totalizadores

    def get_breadcrumb(self):
        investimento_cooperativa = {
            "name": "Investimentos por cooperativa",
            "slug": "investimento_cooperativa",
            "url_name": "investimento_cooperativa",
        }

        return make_breadcrumb([financeiro, investimento_cooperativa])
