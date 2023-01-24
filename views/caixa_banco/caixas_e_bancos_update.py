from django.views.generic.edit import UpdateView

from core.views import AcessoGeralView

from ...forms import CaixaBancoForm, DadoBancarioForm
from ...models import CaixaBanco


class CaixaBancoUpdate(AcessoGeralView, UpdateView):
    model = CaixaBanco

    form_class = CaixaBancoForm

    template_name = "financeiro/caixa_banco/caixas_e_bancos_form.html"

    def get_success_url(self):
        from global_functions.redirect import reverse_lazy_plus

        return reverse_lazy_plus(
            "caixas_e_bancos_detail",
            url_params=[self.object.id],
            get_params={
                "mensagem_toastify": "Conta Caixa alterada com sucesso!"
            },
            just_uri=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["form_dado_bancario"] = DadoBancarioForm(
            instance=self.object.dadobancario
        )

        context["title"] = "Alterar dados"

        return context

    def form_valid(self, form):
        form_dado_bancario = DadoBancarioForm(
            self.request.POST,
            instance=self.object.dadobancario,
        )
        if form_dado_bancario.is_valid() and form.is_valid():
            form.save()
            form_dado_bancario.save()

        return super().form_valid(form)

    def get_breadcrumb(view):
        from global_functions.breadcrumb import make_breadcrumb
        from global_functions.breadcrumb.itens import (
            alterar_dados,
            caixas_bancos,
            financeiro,
            make_detalhes,
        )

        detalhes = make_detalhes(
            "caixas_e_bancos_detail",
            [view.object.id],
        )

        return make_breadcrumb(
            [financeiro, caixas_bancos, detalhes, alterar_dados]
        )
