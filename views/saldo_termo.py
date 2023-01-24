from contratos.models import Empresa, TermoCooperacaoNivel4
from core.views import AcessoGeralView, BaseListView
from django.shortcuts import get_object_or_404
from financeiro.forms import FiltroSaldoTermoForm


class SaldoTermoView(AcessoGeralView, BaseListView):
    model = TermoCooperacaoNivel4

    template_name = "financeiro/saldo_termo/saldo_termo.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        empresa = self.get_empresa()
        context["title"] = f"Saldo dos termos da empresa {empresa}"
        context["filtro_saldo_termo_form"] = FiltroSaldoTermoForm(
            self.request.GET
        )

        context["empresa"] = empresa

        return context

    def get_queryset(self):
        default_query = super().get_queryset()

        empresa = self.get_empresa()
        default_query = default_query.filter(empresa=empresa)

        ano_termo = self.request.GET.get("ano_termo", None)
        if ano_termo:
            inicio_termo = ano_termo.split("-")[0]
            fim_termo = ano_termo.split("-")[1]
            default_query = default_query.filter(
                inicio_termo__year__gte=inicio_termo,
                fim_termo__year__lte=fim_termo,
            )

        situacao = self.request.GET.get("situacao", None)
        if situacao:
            default_query = default_query.filter(situacao=situacao)

        saldo_negativo_total = self.request.GET.get(
            "saldo_negativo_total", False
        )
        if saldo_negativo_total:
            ids_saldo_negativo_total = [
                termo.id for termo in default_query if termo.saldo_atual < 0
            ]
            default_query = default_query.filter(
                id__in=ids_saldo_negativo_total
            )

        saldo_positivo_total = self.request.GET.get(
            "saldo_positivo_total", False
        )
        if saldo_positivo_total:
            ids_saldo_positivo_total = [
                termo.id for termo in default_query if termo.saldo_atual > 0
            ]
            default_query = default_query.filter(
                id__in=ids_saldo_positivo_total
            )

        saldo_negativo_ppt = self.request.GET.get("saldo_negativo_ppt", False)
        if saldo_negativo_ppt:
            ids_saldo_negativo_ppt = [
                termo.id
                for termo in default_query
                if termo.saldo_atual_ppt < 0
            ]
            default_query = default_query.filter(id__in=ids_saldo_negativo_ppt)

        saldo_negativo_capacitacao = self.request.GET.get(
            "saldo_negativo_capacitacao", False
        )
        if saldo_negativo_capacitacao:
            ids_saldo_negativo_capacitacao = [
                termo.id
                for termo in default_query
                if termo.saldo_atual_capacitacao < 0
            ]
            default_query = default_query.filter(
                id__in=ids_saldo_negativo_capacitacao
            )

        saldo_negativo_divulgacao = self.request.GET.get(
            "saldo_negativo_divulgacao", False
        )
        if saldo_negativo_divulgacao:
            ids_saldo_negativo_divulgacao = [
                termo.id
                for termo in default_query
                if termo.saldo_atual_divulgacao < 0
            ]
            default_query = default_query.filter(
                id__in=ids_saldo_negativo_divulgacao
            )

        saldo_negativo_equipamentos = self.request.GET.get(
            "saldo_negativo_equipamentos", False
        )
        if saldo_negativo_equipamentos:
            ids_saldo_negativo_equipamentos = [
                termo.id
                for termo in default_query
                if termo.saldo_atual_equipamentos < 0
            ]
            default_query = default_query.filter(
                id__in=ids_saldo_negativo_equipamentos
            )

        return default_query

    def get_empresa(self):
        empresa_id = self.request.GET.get("empresa", None)
        if empresa_id:
            return get_object_or_404(Empresa, pk=empresa_id)
        else:
            try:
                empresa_default = (
                    FiltroSaldoTermoForm()
                    .fields["empresa"]
                    .choices.queryset[0]
                )
                return empresa_default
            except IndexError:
                return None

    def get_breadcrumb(self):
        from global_functions.breadcrumb import make_breadcrumb
        from global_functions.breadcrumb.itens import financeiro

        saldo_termo = {
            "name": "Saldo dos termos",
            "slug": "saldo_termo",
            "url_name": "saldo_termo",
        }
        return make_breadcrumb([financeiro, saldo_termo])
