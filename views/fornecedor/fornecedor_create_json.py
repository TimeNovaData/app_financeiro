import json

from contratos.forms import EmpresaForm
from core.forms import EnderecoForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def fornecedor_create_json(request):
    data = json.loads(request.body.decode("utf-8"))

    endereco_form = EnderecoForm(data.get("fields_endereco", None))
    if not endereco_form.is_valid():
        return JsonResponse({"error": "Dados do endereço inválidos"})

    fornecedor_form = EmpresaForm(data.get("fields_fornecedor", None))
    if fornecedor_form.is_valid():
        fornecedor = fornecedor_form.save()

        endereco = endereco_form.save()
        endereco.fornecedor = fornecedor
        endereco.save()
    else:
        return JsonResponse({"error": "Dados do fornecedor inválidos"})

    return JsonResponse(
        {
            "message": "Fornecedor cadastrado com sucesso!",
            "id": fornecedor.id,
        }
    )
