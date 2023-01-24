from django import template

register = template.Library()


@register.filter
def get_color_class_fluxo_caixa(value):
    if value < 0:
        return "red"
    else:
        return "green"


@register.simple_tag
def get_saldo_termo_cooperacao(termo, tipo):
    return termo.saldos(tipo)
