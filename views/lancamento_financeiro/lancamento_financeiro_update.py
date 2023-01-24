from datetime import datetime, timedelta

from core.models import Estado
from core.views import AcessoGeralView
from django.views.generic.edit import UpdateView
from global_functions.breadcrumb import make_breadcrumb
from global_functions.breadcrumb.itens import (
    alterar_dados,
    financeiro,
    lancamentos,
    make_detalhes,
)
from global_functions.utils import gerenciar_inline_form

from ...forms import (
    ItemRateioInlineFormSet,
    LancamentoFinanceiroForm,
    ParcelaInlineFormSet,
)
from ...models import LancamentoFinanceiro


class LancamentoFinanceiroUpdateView(AcessoGeralView, UpdateView):
    model = LancamentoFinanceiro

    form_class = LancamentoFinanceiroForm

    template_name = "financeiro/lancamento_financeiro/lancamento_financeiro_form/lancamento_financeiro_form.html"  # noqa E501

    def get_initial(self):
        return {
            "tipo": self.get_tipo(),
        }

    def get_success_url(self):
        from global_functions.redirect import reverse_lazy_plus

        return reverse_lazy_plus(
            "lancamento_financeiro_detail",
            url_params=[
                self.object.pk,
            ],
            get_params={
                "mensagem_toastify": "Lançamento editado com sucesso!",
                "tipo": self.get_tipo(),
            },
            just_uri=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Editar lançamento"
        context["estados"] = Estado.objects.all()

        context["tipo"] = self.get_tipo()

        context["parcela_inline_formset"] = ParcelaInlineFormSet(
            instance=self.object,
        )

        context["item_rateio_inline_formset"] = ItemRateioInlineFormSet(
            instance=self.object.rateio,
        )

        context["possui_parcelas"] = self.get_object().parcela_set.exists()
        rateio = self.get_object().rateio
        if rateio:
            context["possui_itens_rateio"] = rateio.itemrateio_set.exists()
        else:
            context["possui_itens_rateio"] = False

        context["in_fifteen_days"] = (
            datetime.today() + timedelta(days=15)
        ).strftime("%Y-%m-%d")

        return context

    def form_valid(self, form):
        default_return = super().form_valid(form)
        self.object.gerar_rateio()

        parcela_inline_formset = ParcelaInlineFormSet(
            self.request.POST,
            instance=self.object,
        )
        gerenciar_inline_form(parcela_inline_formset)

        item_rateio_inline_formset = ItemRateioInlineFormSet(
            self.request.POST,
            instance=self.object.rateio,
        )
        gerenciar_inline_form(item_rateio_inline_formset)

        return default_return

    def get_tipo(self):
        return self.request.GET.get("tipo", "Despesa")

    def get_breadcrumb(view):
        detalhes = make_detalhes(
            "lancamento_financeiro_detail",
            url_params=[view.object.pk],
            get_params={
                "tipo": view.get_tipo(),
            },
        )

        return make_breadcrumb(
            [financeiro, lancamentos, detalhes, alterar_dados]
        )
