from django.db import models


class AnoContabil(models.Model):
    '''
    A classe AnoContabil serve para registrarmos os anos contábeis.
    Além de fazer as implementações relacionadas a um único ano contábil.
    '''

    nome = models.CharField(
        verbose_name='Nome',
        max_length=100
    )

    data_inicial = models.DateField(
        verbose_name='Data inicial'
    )

    data_final = models.DateField(
        verbose_name='Data final'
    )

    aberto = models.BooleanField(
        verbose_name='Aberto?',
        default=False
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Ano contábil'
        verbose_name_plural = 'Anos contábeis'
