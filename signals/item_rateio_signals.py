from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import ItemRateio


@receiver(post_save, sender=ItemRateio)
def item_rateio_post_save(sender, instance, created, **kwargs):
    if created:
        instance.atualizar_saldo_termo_cooperacao()
