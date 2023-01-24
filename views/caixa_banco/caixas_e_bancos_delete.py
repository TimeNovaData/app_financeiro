from django.views.generic.edit import DeleteView

from core.views import AcessoGeralView

from ...models import CaixaBanco


class CaixaBancoDelete(AcessoGeralView, DeleteView):
    model = CaixaBanco
    need_breadcrumb = False
    template_name = "financeiro/caixa_banco/caixas_e_bancos_delete.html"

    def get_success_url(self):
        from global_functions.redirect import reverse_lazy_plus

        return reverse_lazy_plus(
            "caixas_e_bancos",
            get_params={
                "mensagem_toastify": "Caixa e Bancos excluída com sucesso!"
            },
            just_uri=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Remover Caixa e Bancos"

        return context
