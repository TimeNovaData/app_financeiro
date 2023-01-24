from django.views.generic.edit import UpdateView

from core.views import AcessoGeralView

from ...forms import ContaNivel1Form
from ...models import ContaNivel1


class ContaNivel1Update(AcessoGeralView, UpdateView):
    model = ContaNivel1

    form_class = ContaNivel1Form

    template_name = "financeiro/conta_nivel1/conta_nivel1_form.html"

    def get_success_url(self):
        from global_functions.redirect import reverse_lazy_plus

        return reverse_lazy_plus(
            "conta_nivel1",
            get_params={
                "mensagem_toastify": "Conta gerencial nível 1 alterada com sucesso!"
            },
            just_uri=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Editar contas gerenciais nível 1"

        return context

    def get_breadcrumb(self):
        from global_functions.breadcrumb import make_breadcrumb
        from global_functions.breadcrumb.itens import cadastros, financeiro

        grupo_conta = {
            "name": "Grupo de contas",
            "slug": "grupo_conta",
            "url_name": "conta_nivel1",
        }

        editar_conta_nivel1 = {
            "name": "Editar conta gerencial nível 1",
            "slug": "editar_conta_nivel1",
            "url_name": "",
        }

        return make_breadcrumb(
            [financeiro, cadastros, grupo_conta, editar_conta_nivel1]
        )
