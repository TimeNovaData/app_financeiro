from datetime import datetime, timedelta
from functools import reduce

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum

from ..managers import LancamentoFinanceiroManager
from .caixa_banco import CaixaBanco
from .conta_nivel4 import ContaNivel4
from .tipo_documento_financeiro import TipoDocumentoFinanceiro


class LancamentoFinanceiro(models.Model):
    """
    A classe LancamentoFinanceiro serve para armazernar
    os(as) lançamentos financeiros do sistema.

    Além de fazer as implementações relacionadas a um(a)
    único(a) objeto do tipo LancamentoFinanceiro.
    """

    RECEITA_DESPESA_CHOICES = (
        ("Receita", "Receita"),
        ("Despesa", "Despesa"),
    )

    DATA_REFERENCIA_CHOICES = (
        ("Fixa", "Fixa"),
        (
            "De acordo com data de vencimento",
            "De acordo com data de vencimento",
        ),
    )

    FORMA_PAGAMENTO_CHOICES = (
        ("À vista", "À vista"),
        ("Parcelado", "Parcelado"),
    )

    DESTINACAO_CHOICES = (
        ("Equipamento", "Equipamento"),
        ("Divulgação", "Divulgação"),
        ("Capacitação", "Capacitação"),
    )

    conta_gerencial = models.ForeignKey(
        ContaNivel4,
        verbose_name="Conta gerencial",
        null=True,
        on_delete=models.CASCADE,
    )

    conta_caixa = models.ForeignKey(
        CaixaBanco,
        verbose_name="Conta do banco",
        null=True,
        on_delete=models.CASCADE,
        limit_choices_to={"nao_aceita_lancamentos": False},
    )

    tipo_documento = models.ForeignKey(
        TipoDocumentoFinanceiro,
        verbose_name="Tipo de documento",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    numero_nota_fiscal = models.CharField(
        verbose_name="Número da nota fiscal",
        max_length=20,
        null=True,
        blank=True,
    )

    observacoes_nota_fiscal = models.TextField(
        verbose_name="Observações sobre a nota fiscal",
        null=True,
        blank=True,
    )

    tipo = models.CharField(
        verbose_name="Tipo",
        max_length=50,
        choices=RECEITA_DESPESA_CHOICES,
    )

    anotacoes = models.TextField(
        verbose_name="Anotações",
        null=True,
        blank=True,
    )

    data_referencia = models.DateField(
        verbose_name="Data de referência",
        null=True,
        blank=True,
    )

    data_referencia_parcelas = models.CharField(
        verbose_name="Data de referência das parcelas",
        max_length=100,
        null=True,
        blank=True,
        choices=DATA_REFERENCIA_CHOICES,
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data de criação",
        auto_now_add=True,
        null=True,
    )

    valor_total = models.DecimalField(
        verbose_name="Valor total",
        max_digits=15,
        decimal_places=2,
    )

    forma_pagamento = models.CharField(
        verbose_name="Forma de pagamento",
        max_length=100,
        null=True,
        choices=FORMA_PAGAMENTO_CHOICES,
    )

    impostos = models.DecimalField(
        verbose_name="Impostos",
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True,
    )

    usuario_criacao = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Usuário de criação",
        blank=True,
        null=True,
    )

    usuario_atualizacao = models.ForeignKey(
        User,
        related_name="%(class)s_requests_modified",
        verbose_name="Usuário de atualização",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    objects = LancamentoFinanceiroManager()

    @property
    def proxima_parcela(self):
        return self.parcela_set.filter(data_pagamento__isnull=True).first()

    @property
    def vencimento_proxima_parcela(self):
        """
        Retorna a data do vencimento da próxima parcela do finaneiro.
        """

        proxima_parcela = self.proxima_parcela
        if proxima_parcela:
            return proxima_parcela.data_vencimento
        else:
            return None

    @property
    def previsao_pagamento_proxima_parcela(self):
        """
        Retorna a data da previsão de pagamento da próxima
        parcela do finaneiro.
        """

        proxima_parcela = self.proxima_parcela
        if proxima_parcela:
            return proxima_parcela.data_vencimento
        else:
            return None

    @property
    def parcelas_em_aberto(self):
        """
        Retorna a quantidade de parcelas sem data de pagamento.
        """

        return self.parcela_set.filter(data_pagamento__isnull=True).count()

    @property
    def valor_efetivo(self):
        return (self.valor_total or 0) + (self.impostos or 0)

    @property
    def valor_pendente(self):
        return self.valor_efetivo - self.valor_pago

    @property
    def valor_parcela(self):
        """
        Retorna o valor da parcela do financeiro.
        """
        first_parcela = self.parcela_set.first()
        if first_parcela:
            return first_parcela.valor
        else:
            return 0.00

    @property
    def valor_pago(self):
        def somar_valores(acc, parcela):
            return acc + parcela.valor_efetivo

        valor_pago = reduce(
            somar_valores,
            self.parcela_set.filter(data_pagamento__isnull=False),
            0,
        )
        return round(valor_pago, 2)

    @property
    def pago(self):
        """
        Flag que retorna se o lançamento está pago ou não.
        """

        existe_parcela = self.parcela_set.exists()
        if not existe_parcela:
            return False

        existe_parcela_sem_pagamento = self.parcela_set.filter(
            data_pagamento__isnull=True
        ).exists()
        if existe_parcela_sem_pagamento:
            return False

        return True

    @property
    def data_vencimento(self):
        """
        Retorna a data de vencimento do financeiro com base na data
        de vencimento da última parcela.
        """
        if self.parcela_set.exists():
            return self.parcela_set.last().data_vencimento
        else:
            return None

    @property
    def condicao_pagamento(self):
        """
        Property para retornar a condição em que o pagamento foi feito.
        Seja à vista, 2x ou Nx.
        """

        if self.parcela_set.count() == 0:
            return "Nenhuma parcela encontrada"
        elif self.parcela_set.count() == 1:
            return "À vista"
        else:
            return f"{self.parcela_set.count()}x"

    @property
    def desconto_total(self):
        """
        Retorna o valor total de desconto do financeiro.
        """

        desconto = (
            self.parcela_set.all().aggregate(
                total=Sum("desconto"),
            )["total"]
            or 0
        )

        return desconto

    @property
    def acrescimo_total(self):
        """
        Retorna o valor total de acréscimo do financeiro.
        """

        acrescimo = (
            self.parcela_set.all().aggregate(
                total=Sum("acrescimo"),
            )["total"]
            or 0
        )

        return acrescimo

    def gerar_parcelas(self, numero_parcelas=1) -> None:
        """
        Gera as parcelas de acordo com o número de parcelas.\n
        A primeira parcela possui data de vencimento daqui a 15 dias,
        as demais são geradas com um intervalo de 30 dias.
        """
        valor_parcela = round(self.valor_total / numero_parcelas, 2)

        hoje = datetime.today()
        data_vencimento = hoje + timedelta(days=15)
        for i in range(numero_parcelas):
            self.parcela_set.create(
                lancamento_financeiro=self,
                valor=valor_parcela,
                data_vencimento=data_vencimento,
            )
            data_vencimento += timedelta(days=30)

    def save(self, *args, **kwargs):
        from crum import get_current_user
        from global_functions.utils.save import create_logs, get_changes

        from .log_alteracoes_lancamento_financeiro import (
            LogAlteracoesLancamentoFinanceiro,
        )

        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user

        if self.pk:
            mudancas = get_changes(self)
            # kwargs['update_fields'] = mudancas.normais

            create_logs(
                parent_object=self,
                back_update_fields=mudancas.back,
                old_and_new_object=mudancas.old_and_new_object,
                log_class=LogAlteracoesLancamentoFinanceiro,
                fk_name="lancamento_financeiro",
            )
        super(LancamentoFinanceiro, self).save(*args, **kwargs)

    def __str__(self):
        return f"Lançamento financeiro {self.id}"

    class Meta:
        app_label = "financeiro"
        verbose_name = "Lançamento financeiro"
        verbose_name_plural = "Lançamentos financeiros"
        ordering = ["-id"]
