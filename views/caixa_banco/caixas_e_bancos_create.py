from django.views.generic.edit import CreateView

from core.views import AcessoGeralView

from ...forms import CaixaBancoForm, DadoBancarioForm
from ...models import CaixaBanco, DadoBancario


class CaixaBancoCreate(AcessoGeralView, CreateView):
    model = CaixaBanco
    dadobancario = None
    form_class = CaixaBancoForm

    template_name = "financeiro/caixa_banco/caixas_e_bancos_form.html"

    def get_success_url(self):
        if self.object and self.dadobancario:
            self.dadobancario.caixa_banco = self.object
            self.dadobancario.save()

        from global_functions.redirect import reverse_lazy_plus

        return reverse_lazy_plus(
            "caixas_e_bancos",
            get_params={
                "mensagem_toastify": "Conta Caixa adicionada com sucesso!"
            },
            just_uri=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        self.dadobancario = DadoBancario.objects.create()
        context["form_dado_bancario"] = DadoBancarioForm(
            instance=self.dadobancario
        )

        context["title"] = "Cadastro de conta caixa"

        return context

    def form_valid(self, form):
        """form_dado_bancario = DadoBancarioForm(self.request.POST)
        if form_dado_bancario.is_valid() and form.is_valid():
            dado_bancario = form_dado_bancario.save()
            self.object = form.save()
            self.object.dados_bancarios = dado_bancario
            self.object.save()"""

        dado_bancario_form = DadoBancarioForm(
            self.request.POST, instance=self.dadobancario
        )
        if dado_bancario_form.is_valid():
            self.dadobancario: DadoBancario = dado_bancario_form.save()

        return super().form_valid(form)

    def get_breadcrumb(self):
        from global_functions.breadcrumb import make_breadcrumb
        from global_functions.breadcrumb.itens import caixas_bancos, financeiro

        cadastrar_caixas_bancos = {
            "name": "Cadastrar caixa e banco",
            "slug": "cadastrar_caixas_bancos",
            "url_name": "",
        }

        return make_breadcrumb(
            [financeiro, caixas_bancos, cadastrar_caixas_bancos]
        )
