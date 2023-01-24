import math
# import threading

import pandas
from contratos.models import Empresa
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def importador_conta_gerencial(request):
    error = False

    if request.method == "POST":
        tabela_file = request.FILES["tabela"]
        try:
            tabela_excel = pandas.read_excel(io=tabela_file, engine="openpyxl")
            # tabela_excel = pandas.read_csv(tabela_file)
        except Exception:
            tabela_excel = None
            error = True

        if not error:
            # Cuidado, linha abaixo exclui a base existente
            # Empresa.objects.all().delete()

            # t = threading.Thread(
            #     target=importacao_conta_gerencial,
            #     args=[tabela_excel],
            #     daemon=True,
            # )
            # t.start()
            importacao_conta_gerencial(tabela_excel)

    context = {"error": error}

    return render(
        request, "financeiro/importador_conta_gerencial.html", context
    )


def importacao_conta_gerencial(tabela_excel):
    lista_conta_gerencials = []
    for i, empresa in enumerate(tabela_excel.values):
        print(i)
        print(type(empresa[12]))
        lista_conta_gerencials.append(
            Empresa(
                # indice=empresa[0],
                nome=empresa[1],
                razao_social=empresa[2],
                email=empresa[3] if not empresa[3] else None,
                telefone=empresa[4] if not empresa[4] else None,
                logo=empresa[5] if not empresa[5] else None,
                site=empresa[6] if not empresa[6] else None,
                contato=empresa[7] if not empresa[7] else None,
                cnpj=int(empresa[8]) if not math.isnan(empresa[8]) else None,
                inscricao_estadual=empresa[9]
                if not math.isnan(empresa[9])
                else None,
                #
                inscricao_municipal=empresa[10]
                if not math.isnan(empresa[10])
                else None,
                #
                responsavel_mercadoria=empresa[11],
                tecnico_responsavel=empresa[12]
                if not math.isnan(empresa[12])
                else None,
                #
                # usuarios_com_acesso=empresa[13] if not math.isnan(
                # empresa[13]
                # ) else [],
                # valor_tonelada=Decimal(empresa[14] or 0) ,
                # pagamento_tonelada=Decimal(empresa[15] or 0) ,
                is_cooperativa=int(empresa[16]),
                is_fornecedor=int(empresa[17]),
            )
        )

    print("começou")
    Empresa.objects.bulk_create(lista_conta_gerencials)
    print("acabou")
