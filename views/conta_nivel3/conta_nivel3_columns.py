from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from global_functions.async_table.columns.conta_nivel3.get_columns import (
    get_columns_conta_nivel3,
)


@login_required
def conta_nivel3_columns(request):
    data = {"columns": get_columns_conta_nivel3()}

    return JsonResponse(data)
