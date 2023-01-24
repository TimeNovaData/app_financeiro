from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def resumo_financeiro(request):
    context = {
        'title': 'Resumo',
    }

    return render(
        request,
        'financeiro/resumo_financeiro.html',
        context
    )
