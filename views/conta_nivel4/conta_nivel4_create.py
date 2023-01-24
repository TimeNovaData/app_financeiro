from django.views.generic.edit import CreateView

from core.views import AcessoGeralView

from ...forms import ContaNivel4Form
from ...models import ContaNivel4


class ContaNivel4Create(AcessoGeralView, CreateView):
    model = ContaNivel4

    form_class = ContaNivel4Form

    template_name = "financeiro/conta_nivel4/conta_nivel4_form.html"

    def get_success_url(self):
        from global_functions.redirect import reverse_lazy_plus

        return reverse_lazy_plus(
            "conta_nivel4",
            get_params={
                "mensagem_toastify": "Conta gerencial nível 4 adicionada com sucesso!"
            },
            just_uri=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Nova conta gerencial nível 4"

        return context

    def get_breadcrumb(self):
        from global_functions.breadcrumb import make_breadcrumb
        from global_functions.breadcrumb.itens import cadastros, financeiro

        grupo_conta = {
            "name": "Grupo de contas",
            "slug": "grupo_conta",
            "url_name": "conta_nivel4",
        }

        nova_conta_nivel4 = {
            "name": "Nova conta gerencial nível 4",
            "slug": "nova_conta_nivel4",
            "url_name": "",
        }

        return make_breadcrumb(
            [financeiro, cadastros, grupo_conta, nova_conta_nivel4]
        )
