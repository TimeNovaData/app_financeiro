from django.views.generic.edit import DeleteView

from core.views import AcessoGeralView

from ...models import Rateio


class RateioDeleteView(AcessoGeralView, DeleteView):
    model = Rateio
    need_breadcrumb = False
    template_name = "financeiro/rateio/rateio_delete.html"

    def get_success_url(self):
        from global_functions.redirect import reverse_lazy_plus

        return reverse_lazy_plus(
            "rateio_list",
            get_params={
                "mensagem_toastify": "Rateio excluído com sucesso!",
            },
            just_uri=True,
        )
