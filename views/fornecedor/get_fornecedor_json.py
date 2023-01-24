from contratos.models import Empresa
from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.http import JsonResponse


@login_required
def get_fornecedor_json(request):
    id_fornecedor = request.GET.get("id_fornecedor", None)

    try:
        fornecedor = Empresa.objects.get(id=id_fornecedor)
        fornecedor_json = model_to_dict(
            fornecedor,
            exclude=[
                "logo",
                "tecnico_responsavel",
                "usuarios_com_acesso",
            ],
        )

        return JsonResponse(
            {
                "message": "Fornecedor encontrado!",
                "fornecedor": fornecedor_json,
            }
        )
    except Empresa.DoesNotExist:
        return JsonResponse({"error": "Fornecedor não encontrado"})
