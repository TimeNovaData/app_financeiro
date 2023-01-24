from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from global_functions.async_table.columns_itens import delete_link, update_link

@login_required
def caixa_banco_columns(request):
    nome = {
        "id": "nome",
        "order": 0,
        "name": "Nome da conta",
        
    }

    tipo_conta = {
        "id": "tipo_conta",
        "order": 1,
        "name": "Tipo da conta",
        
    }

    periodo_abertura = {
        "id": "periodo_abertura",
        "order": 2,
        "name": "Abertura",
        
    }

    periodo_encerramento = {
        "id": "periodo_encerramento",
        "order": 3,
        "name": "Encerramento",
        
    }

    considerar_fluxo_caixa_str = {
        "id": "considerar_fluxo_caixa_str",
        "order": 4,
        "name": "Fluxo de caixa",
        
    }


    data = {
        "columns": [
            nome,
            tipo_conta,
            periodo_abertura,
            periodo_encerramento,
            considerar_fluxo_caixa_str,         
            update_link(order=5),
            delete_link(order=6),
        ]
    }

    return JsonResponse(data)

