from django.views.generic.edit import UpdateView

from core.views import AcessoGeralView
from global_functions.breadcrumb import make_breadcrumb
from global_functions.breadcrumb.itens import (
    alterar_dados,
    financeiro,
    parcelas,
)

from ...forms import ParcelaForm
from ...models import Parcela


class ParcelaUpdateView(AcessoGeralView, UpdateView):
    model = Parcela

    form_class = ParcelaForm

    template_name = "financeiro/parcela/parcela_form.html"

    def get_success_url(self):
        from global_functions.redirect import reverse_lazy_plus

        return reverse_lazy_plus(
            "parcela_list",
            get_params={
                "mensagem_toastify": "Parcela editada com sucesso!",
            },
            just_uri=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Editar parcela"

        return context

    def get_breadcrumb(self):
        return make_breadcrumb(
            [
                financeiro,
                parcelas,
                alterar_dados,
            ]
        )
