from django.views.generic.edit import UpdateView

from core.views import AcessoGeralView

from ...forms import ContaNivel2Form
from ...models import ContaNivel2


class ContaNivel2Update(AcessoGeralView, UpdateView):
    model = ContaNivel2

    form_class = ContaNivel2Form

    template_name = "financeiro/conta_nivel2/conta_nivel2_form.html"

    def get_success_url(self):
        from global_functions.redirect import reverse_lazy_plus

        return reverse_lazy_plus(
            "conta_nivel2",
            get_params={
                "mensagem_toastify": "Conta gerencial nível 2 alterada com sucesso!"
            },
            just_uri=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Editar contas gerenciais nível 2"

        return context

    def get_breadcrumb(self):
        from global_functions.breadcrumb import make_breadcrumb
        from global_functions.breadcrumb.itens import cadastros, financeiro

        grupo_conta = {
            "name": "Grupo de contas",
            "slug": "grupo_conta",
            "url_name": "conta_nivel2",
        }

        editar_conta_nivel2 = {
            "name": "Editar conta gerencial nível 2",
            "slug": "editar_conta_nivel2",
            "url_name": "",
        }

        return make_breadcrumb(
            [financeiro, cadastros, grupo_conta, editar_conta_nivel2]
        )
