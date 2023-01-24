from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView

from core.views import AcessoGeralView

from ...models import LancamentoFinanceiro


class LancamentoFinanceiroDeleteView(AcessoGeralView, DeleteView):
    model = LancamentoFinanceiro
    need_breadcrumb = False
    template_name = (
        "financeiro/lancamento_financeiro/lancamento_financeiro_delete.html"
    )

    def get_success_url(self):
        from global_functions.redirect import reverse_lazy_plus

        return reverse_lazy_plus(
            "lancamento_financeiro_list",
            get_params={
                "mensagem_toastify": "Lancamento excluído com sucesso!",
                "tipo": self.get_tipo(),
            },
            just_uri=True,
        )

    def get_tipo(self):
        return self.request.GET.get("tipo", "Despesa")
