# Deixou de ser usado dia 03/12/2022
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# from ..models import Parcela


# @receiver(post_save, sender=Parcela)
# def parcela_post_save(sender, instance, created, **kwargs):
#     if created:
#         instance.lancamento_financeiro.atualizar_saldo_termo_cooperacao()
