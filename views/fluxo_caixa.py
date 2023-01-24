from core.views import AcessoGeralView
from django.db.models import Q
from django.views.generic import TemplateView
from financeiro.forms import FiltroFluxoCaixaForm
from financeiro.models import Parcela
from global_functions.charts import ChartPerTimeCourse


class FluxoCaixaView(AcessoGeralView, TemplateView):
    template_name = "financeiro/fluxo_caixa/fluxo_caixa.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filtro_form"] = FiltroFluxoCaixaForm(self.request.GET)

        tipo_periodo = self.request.GET.get("tipo_periodo", "Mensal")
        tipo_periodo = "Mensal" if not tipo_periodo else tipo_periodo

        date_field = self.get_date_field()
        pre_filter_objects = self.get_pre_filter_objects(date_field)

        values = ChartPerTimeCourse(
            pre_filter_objects=pre_filter_objects,
            date_field=date_field,
            decimal_field="valor_efetivo",
            tipo_periodo=tipo_periodo,
            receita_despesa_field="lancamento_financeiro__tipo",
        ).values

        context["values"] = values
        return context

    def get_date_field(self):
        somente_provisionadas = self.request.GET.get(
            "somente_provisionadas", False
        )
        if somente_provisionadas:
            date_field = "data_vencimento"
        else:
            date_field = "data_pagamento"

        return date_field

    def get_pre_filter_objects(self, date_field):
        query = Parcela.objects.all()

        if date_field == "data_vencimento":
            query = query.exclude(data_pagamento__isnull=False)

        query = self.filter_datas(query)
        query = self.filter_projetos(query)
        query = self.filter_contas(query)

        return query

    def filter_datas(self, query):
        data_inicial = self.request.GET.get("data_inicial", None)
        data_final = self.request.GET.get("data_final", None)

        if data_inicial:
            query = query.filter(data_pagamento__gte=data_inicial)
        if data_final:
            query = query.filter(data_pagamento__lte=data_final)

        return query

    def filter_projetos(self, query):
        projeto_nivel1 = self.request.GET.get("projetos_nivel1", None)
        projeto_nivel2 = self.request.GET.get("projetos_nivel2", None)
        projeto_nivel3 = self.request.GET.get("projetos_nivel3", None)
        projeto_nivel4 = self.request.GET.get("projetos_nivel4", None)

        if (
            projeto_nivel1
            or projeto_nivel2
            or projeto_nivel3
            or projeto_nivel4
        ):
            projeto_nivel4_expression = (
                "lancamento_financeiro__compra__termo_cooperacao"
            )
            projeto_nivel3_expression = (
                f"{projeto_nivel4_expression}__termo_cooperacao_nivel3"
            )
            projeto_nivel2_expression = (
                f"{projeto_nivel3_expression}__termo_cooperacao_nivel2"
            )
            projeto_nivel1_expression = (
                f"{projeto_nivel2_expression}__termo_cooperacao_nivel1"
            )

        if projeto_nivel1:
            expression = Q(
                (
                    projeto_nivel1_expression,
                    projeto_nivel1,
                )
            )
            query = query.filter(expression)
        if projeto_nivel2:
            expression = Q(
                (
                    projeto_nivel2_expression,
                    projeto_nivel2,
                )
            )
            query = query.filter(expression)
        if projeto_nivel3:
            expression = Q(
                (
                    projeto_nivel3_expression,
                    projeto_nivel3,
                )
            )
            query = query.filter(expression)
        if projeto_nivel4:
            expression = Q(
                (
                    projeto_nivel4_expression,
                    projeto_nivel4,
                )
            )
            query = query.filter(expression)

        return query

    def filter_contas(self, query):
        conta_nivel1 = self.request.GET.get("contas_nivel1", None)
        conta_nivel2 = self.request.GET.get("contas_nivel2", None)
        conta_nivel3 = self.request.GET.get("contas_nivel3", None)
        conta_nivel4 = self.request.GET.get("contas_nivel4", None)

        if conta_nivel1 or conta_nivel2 or conta_nivel3 or conta_nivel4:
            conta_nivel4_expression = "conta_gerencial"
            conta_nivel3_expression = (
                f"{conta_nivel4_expression}__conta_nivel3"
            )
            conta_nivel2_expression = (
                f"{conta_nivel3_expression}__conta_nivel2"
            )
            conta_nivel1_expression = (
                f"{conta_nivel2_expression}__conta_nivel1"
            )

        if conta_nivel1:
            expression = Q(
                (
                    conta_nivel1_expression,
                    conta_nivel1,
                )
            )
            query = query.filter(expression)
        if conta_nivel2:
            expression = Q(
                (
                    conta_nivel2_expression,
                    conta_nivel2,
                )
            )
            query = query.filter(expression)
        if conta_nivel3:
            expression = Q(
                (
                    conta_nivel3_expression,
                    conta_nivel3,
                )
            )
            query = query.filter(expression)
        if conta_nivel4:
            expression = Q(
                (
                    conta_nivel4_expression,
                    conta_nivel4,
                )
            )
            query = query.filter(expression)

        return query

    def get_breadcrumb(self):
        from global_functions.breadcrumb import make_breadcrumb
        from global_functions.breadcrumb.itens import financeiro

        fluxo_caixa = {
            "name": "Fluxo de caixa",
            "slug": "fluxo_caixa",
            "url_name": "fluxo_caixa",
        }
        return make_breadcrumb([financeiro, fluxo_caixa])
