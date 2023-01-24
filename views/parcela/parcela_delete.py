from django.views.generic.edit import DeleteView

from core.views import AcessoGeralView

from ...models import Parcela


class ParcelaDeleteView(AcessoGeralView, DeleteView):
    model = Parcela
    need_breadcrumb = False
    template_name = "financeiro/parcela/parcela_delete.html"

    def get_success_url(self):
        from global_functions.redirect import reverse_lazy_plus

        return reverse_lazy_plus(
            "parcela_list",
            get_params={
                "mensagem_toastify": "Parcela excluída com sucesso!",
            },
            just_uri=True,
        )
