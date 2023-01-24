from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from global_functions.async_table.columns_itens import delete_link, update_link


@login_required
def tipo_documento_financeiro_columns(request):
    codigo = {
        "id": "codigo",
        "order": 0,
        "name": "Código",
    }

    nome = {
        "id": "nome",
        "order": 1,
        "name": "Nome/Descrição",
    }

    data = {
        "columns": [
            codigo,
            nome,
            update_link(order=2),
            delete_link(order=3),
        ]
    }

    return JsonResponse(data)
