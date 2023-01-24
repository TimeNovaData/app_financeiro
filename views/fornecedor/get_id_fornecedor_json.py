from contratos.models import Empresa
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def get_id_fornecedor_json(request):
    cnpj_fornecedor = request.GET.get("cnpj_fornecedor", None)

    if cnpj_fornecedor:
        fornecedor = Empresa.objects.filter(cnpj=cnpj_fornecedor).first()
        if fornecedor:
            response = {
                "message": "Fornecedor encontrado com sucesso",
                "fornecedor_id": fornecedor.id,
            }
            return JsonResponse(response)

    return JsonResponse(
        {"error": "Fornecedor não encontrado!"}
    )  # Padrão aconselhável
