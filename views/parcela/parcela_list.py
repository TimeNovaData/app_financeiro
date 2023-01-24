from django.db.models import Q

from core.views import AcessoGeralView, BaseListView
from financeiro.forms import FiltroParcelaForm, PagarParcelaForm
from financeiro.models import Parcela
from global_functions.breadcrumb import make_breadcrumb
from global_functions.breadcrumb.itens import financeiro, parcelas
from global_functions.redirect import reverse_lazy_plus


class ParcelaListView(AcessoGeralView, BaseListView):
    model = Parcela

    template_name = "financeiro/parcela/parcela_list.html"

    def get_queryset(self, **kwargs):
        default_return = super().get_queryset(**kwargs)

        tipo = self.request.GET.get("tipo", None)
        data_inicial = self.request.GET.get("data_inicial", None)
        data_final = self.request.GET.get("data_final", None)

        if tipo:
            default_return = default_return.filter(
                lancamento_financeiro__tipo=tipo
            )

        if data_inicial:
            default_return = default_return.filter(
                Q(data_vencimento__gte=data_inicial)
                | Q(data_pagamento__gte=data_inicial)
                | Q(data_referencia__gte=data_inicial)
            )

        if data_final:
            default_return = default_return.filter(
                Q(data_vencimento__lte=data_final)
                | Q(data_pagamento__lte=data_final)
                | Q(data_referencia__lte=data_final)
            )

        return default_return

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["tipo"] = self.request.GET.get("tipo", None)
        context["data_inicial"] = self.request.GET.get("data_inicial", None)
        context["data_final"] = self.request.GET.get("data_final", None)

        context["pagar_parcela_form"] = PagarParcelaForm()
        context["filtro_parcela_form"] = FiltroParcelaForm(self.request.GET)

        return context

    def get_simple_fields_filter(self):
        return [
            "id",
            "lancamento_financeiro__id",
            "caixa_banco_real__nome",
            "conta_gerencial__nome",
            "lancamento_financeiro__tipo",
            "data_referencia",
            "data_vencimento",
            "data_pagamento",
            "valor",
            "acrescimo",
            "desconto",
        ]

    def get_columns(self):
        return {
            "id": "N° da parcela",
            "lancamento_financeiro__id": "Lançamento",
            "caixa_banco_real__nome": "Caixa/banco real",
            "conta_gerencial__nome": "Conta gerencial",
            "lancamento_financeiro__tipo": "Tipo",
            "data_referencia": "Data de referência",
            "data_vencimento": "Data de vencimento",
            "paga_str": "Paga",
            "data_pagamento": "Data de pagamento",
            "valor": "Valor",
            "acrescimo": "Acréscimo",
            "desconto": "Desconto",
            "valor_efetivo": "Valor efetivo",
        }

    def post(self, request, *args, **kwargs):
        string_parcelas = request.POST.get("array-parcelas")
        list_parcelas = string_parcelas.split(",")
        query_parcelas = Parcela.objects.filter(
            id__in=list_parcelas,
            data_pagamento__isnull=True,
        )

        for parcela in query_parcelas:
            pagar_parcela_form = PagarParcelaForm(
                request.POST,
                instance=parcela,
            )
            parcela.pagar(pagar_parcela_form)

        if query_parcelas.count() > 1:
            mensagem_toastify = "Parcelas pagas com sucesso!"
        elif query_parcelas.count() == 1:
            mensagem_toastify = "Parcela paga com sucesso!"
        else:
            mensagem_toastify = "Nenhuma parcela paga!"

        return reverse_lazy_plus(
            "parcela_list",
            get_params={
                "mensagem_toastify": mensagem_toastify,
            },
        )

    def get_breadcrumb(self):
        return make_breadcrumb([financeiro, parcelas])
