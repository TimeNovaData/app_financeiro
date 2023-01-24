from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from global_functions.async_table.columns.conta_nivel1.get_columns import (
    get_columns_conta_nivel1,
)


@login_required
def conta_nivel1_columns(request):
    data = {"columns": get_columns_conta_nivel1()}

    return JsonResponse(data)
