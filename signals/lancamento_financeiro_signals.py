from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from ..models import LancamentoFinanceiro


@receiver(post_save, sender=LancamentoFinanceiro)
def lancamento_financeiro_post_save(sender, instance, created, **kwargs):
    if created:
        instance.gerar_rateio()
        instance.gerar_item_rateio_default()


@receiver(post_delete, sender=LancamentoFinanceiro)
def lancamento_financeiro_post_delete(sender, instance, **kwargs):
    instance.apagar_rateio()
