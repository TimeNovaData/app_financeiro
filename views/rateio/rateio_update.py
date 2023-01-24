from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView

from core.views import AcessoGeralView
from global_functions.breadcrumb import make_breadcrumb
from global_functions.breadcrumb.itens import (
    alterar_dados,
    financeiro,
    rateios,
)
from global_functions.utils import gerenciar_inline_form

from ...forms import ItemRateioInlineFormSet, RateioForm
from ...models import Rateio


class RateioUpdateView(AcessoGeralView, UpdateView):
    model = Rateio

    form_class = RateioForm

    template_name = "financeiro/rateio/rateio_form.html"

    def get_success_url(self):
        from global_functions.redirect import reverse_lazy_plus

        return reverse_lazy_plus(
            "rateio_list",
            get_params={
                "mensagem_toastify": "Rateio editado com sucesso!",
            },
            just_uri=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Editar rateio"

        context["inline_formset"] = ItemRateioInlineFormSet(
            instance=self.object,
        )

        return context

    def form_valid(self, form):
        default_return = super().form_valid(form)

        item_rateio_inline_formset = ItemRateioInlineFormSet(
            self.request.POST,
            instance=self.object,
        )
        gerenciar_inline_form(item_rateio_inline_formset)

        return default_return

    def get_breadcrumb(self):
        return make_breadcrumb(
            [
                financeiro,
                rateios,
                alterar_dados,
            ]
        )
