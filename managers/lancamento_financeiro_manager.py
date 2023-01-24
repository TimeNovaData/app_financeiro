from datetime import datetime, timedelta

from django.db import models


class LancamentoFinanceiroManager(models.Manager):
    '''
    A classe LancamentoFinanceiroManager serve para
    realizar as implementações relacionadas a múltiplos
    objetos do tipo LancamentoFinanceiroManagerno sistema.
    '''

    data_inicial = datetime.today() - timedelta(days=180)

    data_final = datetime.today()

    def lancamentos_periodo(
        self,
        tipo: str = None,
        only_vencidos: bool = False,
        only_pagos: bool = False,
        data_inicial: datetime = data_inicial,
        data_final: datetime = data_final,
    ):
        """
        Função para retornar os lançamentos financeiros
        em determinado período de tempo.

        Arguments:
            tipo: str = None
            Tipo de lançamento financeiro.\n
            Pode ser "Deceita" ou "Despesa".\n
            Em caso de não ser passado o sistema filtra
            ambos.

            only_vencidos: bool = False
            Se True, retorna apenas os lançamentos
            financeiros vencidos.

            only_pagos: bool = False
            Se True, retorna apenas os lançamentos
            financeiros pagos.

            data_inicial: datetime = data_inicial
            Data inicial do período de tempo.\n
            Em caso de não ser passado o sistema filtra
            a partir de 6 meses atrás.

            data_final: datetime = data_final
            Data final do período de tempo.\n
            Em caso de não ser passado o sistema filtra
            até a data atual.
        """

        lancamentos = self.filter(
            data_criacao__range=[data_inicial, data_final]
        )

        if tipo:
            lancamentos = lancamentos.filter(
                tipo=tipo,
            )

        if only_vencidos:
            hoje = datetime.today().date()
            lancamentos = list(filter(
                lambda lancamento: (
                    lancamento.vencimento_proxima_parcela
                    and lancamento.vencimento_proxima_parcela < hoje
                    and not lancamento.pago
                ),
                lancamentos,
            ))

        if only_pagos:
            lancamentos = list(filter(
                lambda lancamento: lancamento.pago,
                lancamentos
            ))

        return lancamentos

    # def lancamentos_dia(self, date: datetime):
    #     """
    #     Função para retornar os lançamentos financeiros
    #     de um determinado dia.
    #     """

    #     return self.filter(
    #         data_criacao=date,
    #     )

    # def lancamentos_mes(self, date: datetime):
    #     """
    #     Função para retornar os lançamentos financeiros
    #     de um determinado mês.
    #     """

    #     return self.filter(
    #         data_criacao__month=date.month,
    #         data_criacao__year=date.year,
    #     )

    # def lancamentos_ano(self, date: datetime):
    #     """
    #     Função para retornar os lançamentos financeiros
    #     de um determinado ano.
    #     """

    #     return self.filter(
    #         data_criacao__year=date.year,
    #     )
