from django.urls import include, path
from financeiro import views, viewsets
from rest_framework import routers

financeiro_router = routers.DefaultRouter()
financeiro_router.register(
    "conta-nivel1",
    viewsets.ContaNivel1ViewSet,
    basename="conta_nivel1",
)

financeiro_router.register(
    "conta-nivel2",
    viewsets.ContaNivel2ViewSet,
    basename="conta_nivel2",
)
financeiro_router.register(
    "conta-nivel3",
    viewsets.ContaNivel3ViewSet,
    basename="conta_nivel3",
)
financeiro_router.register(
    "conta-nivel4",
    viewsets.ContaNivel4ViewSet,
    basename="conta_nivel4",
)
financeiro_router.register(
    "caixa_banco",
    viewsets.CaixaBancoViewSet,
    basename="caixa_banco",
)

financeiro_router.register(
    "tipo_documento_financeiro",
    viewsets.TipoDocumentoFinanceiroViewSet,
    basename="tipo_documento_financeiro",
)

financeiro_router.register(
    "lancamento_financeiro",
    viewsets.LancamentoFinanceiroViewSet,
    basename="lancamento_financeiro",
)

financeiro_router.register(
    "dado_bancario",
    viewsets.DadoBancarioViewSet,
    basename="dado_bancario",
)

financeiro_router.register(
    "forma_pagamento",
    viewsets.FormaPagamentoViewSet,
    basename="forma_pagamento",
)

financeiro_router.register(
    "item_rateio",
    viewsets.ItemRateioViewSet,
    basename="item_rateio",
)

financeiro_router.register(
    "parcela",
    viewsets.ParcelaViewSet,
    basename="parcela",
)

financeiro_router.register(
    "rateio",
    viewsets.RateioViewSet,
    basename="rateio",
)

financeiro_router.register(
    "tipo_conta",
    viewsets.TipoContaViewSet,
    basename="tipo_conta",
)

financeiro_router.register(
    "banco",
    viewsets.BancoViewSet,
    basename="banco",
)

fornecedor_patterns = [
    path(
        "get-fornecedor-json/",
        views.get_fornecedor_json,
        name="get_fornecedor_json",
    ),
    path(
        "fornecedor-create-json/",
        views.fornecedor_create_json,
        name="fornecedor_create_json",
    ),
    path(
        "get-id-fornecedor-json-json/",
        views.get_id_fornecedor_json,
        name="get_id_fornecedor_json",
    ),
]

conta_nivel1_patterns = [
    path(
        "conta-nivel1/",
        views.ContaNivel1ListView.as_view(),
        name="conta_nivel1",
    ),
    path(
        "conta-nivel1-create/",
        views.ContaNivel1Create.as_view(),
        name="conta_nivel1_create",
    ),
    path(
        "conta-nivel1-delete/<int:pk>/",
        views.ContaNivel1Delete.as_view(),
        name="conta_nivel1_delete",
    ),
    path(
        "conta-nivel1-update/<int:pk>/",
        views.ContaNivel1Update.as_view(),
        name="conta_nivel1_update",
    ),
    path(
        "conta-nivel1-columns/",
        views.conta_nivel1_columns,
        name="conta_nivel1_columns",
    ),
]

conta_nivel2_patterns = [
    path(
        "conta-nivel2/",
        views.ContaNivel2ListView.as_view(),
        name="conta_nivel2",
    ),
    path(
        "conta-nivel2-create/",
        views.ContaNivel2Create.as_view(),
        name="conta_nivel2_create",
    ),
    path(
        "conta-nivel2-delete/<int:pk>/",
        views.ContaNivel2Delete.as_view(),
        name="conta_nivel2_delete",
    ),
    path(
        "conta-nivel2-update/<int:pk>/",
        views.ContaNivel2Update.as_view(),
        name="conta_nivel2_update",
    ),
    path(
        "conta-nivel2-columns/",
        views.conta_nivel2_columns,
        name="conta_nivel2_columns",
    ),
]

conta_nivel3_patterns = [
    path(
        "conta-nivel3/",
        views.ContaNivel3ListView.as_view(),
        name="conta_nivel3",
    ),
    path(
        "conta-nivel3-create/",
        views.ContaNivel3Create.as_view(),
        name="conta_nivel3_create",
    ),
    path(
        "conta-nivel3-delete/<int:pk>/",
        views.ContaNivel3Delete.as_view(),
        name="conta_nivel3_delete",
    ),
    path(
        "conta-nivel3-update/<int:pk>/",
        views.ContaNivel3Update.as_view(),
        name="conta_nivel3_update",
    ),
    path(
        "conta-nivel3-columns/",
        views.conta_nivel3_columns,
        name="conta_nivel3_columns",
    ),
]

conta_nivel4_patterns = [
    path(
        "importador-conta-gerencial/",
        views.importador_conta_gerencial,
        name="importador_conta_gerencial",
    ),
    path(
        "conta-nivel4/",
        views.ContaNivel4ListView.as_view(),
        name="conta_nivel4",
    ),
    path(
        "conta-nivel4-create/",
        views.ContaNivel4Create.as_view(),
        name="conta_nivel4_create",
    ),
    path(
        "conta-nivel4-delete/<int:pk>/",
        views.ContaNivel4Delete.as_view(),
        name="conta_nivel4_delete",
    ),
    path(
        "conta-nivel4-update/<int:pk>/",
        views.ContaNivel4Update.as_view(),
        name="conta_nivel4_update",
    ),
]

caixas_e_bancos_patterns = [
    path(
        "caixas-e-bancos/",
        views.CaixaBancoListView.as_view(),
        name="caixas_e_bancos",
    ),
    path(
        "caixas-e-bancos-create/",
        views.CaixaBancoCreate.as_view(),
        name="caixas_e_bancos_create",
    ),
    path(
        "caixas-e-bancos-detail/<int:pk>/",
        views.CaixaBancoDetail.as_view(),
        name="caixas_e_bancos_detail",
    ),
    path(
        "caixas-e-bancos-update/<int:pk>/",
        views.CaixaBancoUpdate.as_view(),
        name="caixas_e_bancos_update",
    ),
    path(
        "caixas-e-bancos-delete/<int:pk>/",
        views.CaixaBancoDelete.as_view(),
        name="caixas_e_bancos_delete",
    ),
    path(
        "caixas-e-bancos-columns/",
        views.caixa_banco_columns,
        name="caixas_e_bancos_columns",
    ),
]

lancamento_financeiro_patterns = [
    path(
        "lancamento-financeiro-detail/<int:pk>/",
        views.LancamentoFinanceiroDetailView.as_view(),
        name="lancamento_financeiro_detail",
    ),
    path(
        "lancamento-financeiro-list/",
        views.LancamentoFinanceiroListView.as_view(),
        name="lancamento_financeiro_list",
    ),
    path(
        "lancamento-financeiro-create/",
        views.LancamentoFinanceiroCreateView.as_view(),
        name="lancamento_financeiro_create",
    ),
    path(
        "lancamento-financeiro-update/<int:pk>/",
        views.LancamentoFinanceiroUpdateView.as_view(),
        name="lancamento_financeiro_update",
    ),
    path(
        "lancamento-financeiro-receita-delete/<int:pk>/",
        views.LancamentoFinanceiroDeleteView.as_view(),
        name="lancamento_financeiro_delete",
    ),
]

parcela_patterns = [
    path(
        "parcela-delete/<int:pk>/",
        views.ParcelaDeleteView.as_view(),
        name="parcela_delete",
    ),
    path(
        "parcela-list/",
        views.ParcelaListView.as_view(),
        name="parcela_list",
    ),
    path(
        "parcela-update/<int:pk>/",
        views.ParcelaUpdateView.as_view(),
        name="parcela_update",
    ),
]

rateio_patterns = [
    # path(
    #     "rateio-create/",
    #     views.RateioCreateView.as_view(),
    #     name="rateio_create",
    # ),
    path(
        "rateio-delete/<int:pk>/",
        views.RateioDeleteView.as_view(),
        name="rateio_delete",
    ),
    path(
        "rateio-list/",
        views.RateioListView.as_view(),
        name="rateio_list",
    ),
    path(
        "rateio-detail/<int:pk>/",
        views.RateioDetailView.as_view(),
        name="rateio_detail",
    ),
    # path(
    #     "rateio-update/<int:pk>/",
    #     views.RateioUpdateView.as_view(),
    #     name="rateio_update",
    # ),
]

tipo_documento_financeiro_patterns = [
    path(
        "tipo-documento-financeiro-create/",
        views.TipoDocumentoFinanceiroCreateView.as_view(),
        name="tipo_documento_financeiro_create",
    ),
    path(
        "tipo-documento-financeiro-delete<int:pk>/",
        views.TipoDocumentoFinanceiroDeleteView.as_view(),
        name="tipo_documento_financeiro_delete",
    ),
    path(
        "tipo-documento-financeiro/",
        views.TipoDocumentoFinanceiroListView.as_view(),
        name="tipo_documento_financeiro_list",
    ),
    path(
        "tipo-documento-financeiro-update/<int:pk>/",
        views.TipoDocumentoFinanceiroUpdateView.as_view(),
        name="tipo_documento_financeiro_update",
    ),
    path(
        "tipo-documento-financeiro-columns/",
        views.tipo_documento_financeiro_columns,
        name="tipo_documento_financeiro_columns",
    ),
]


urlpatterns = (
    [
        path("api/", include(financeiro_router.urls)),
        path(
            "caixas-e-bancos/",
            views.CaixaBancoListView.as_view(),
            name="caixas_e_bancos",
        ),
        path(
            "fluxo-caixa/",
            views.FluxoCaixaView.as_view(),
            name="fluxo_caixa",
        ),
        path(
            "investimento-cooperativa/",
            views.InvestimentoCooperativaListView.as_view(),
            name="investimento_cooperativa",
        ),
        path(
            "",
            views.resumo_financeiro,
            name="resumo_financeiro",
        ),
        path(
            "saldo-termo/",
            views.SaldoTermoView.as_view(),
            name="saldo_termo",
        ),
    ]
    + fornecedor_patterns
    + conta_nivel1_patterns
    + conta_nivel2_patterns
    + conta_nivel3_patterns
    + conta_nivel4_patterns
    + caixas_e_bancos_patterns
    + lancamento_financeiro_patterns
    + parcela_patterns
    + rateio_patterns
    + tipo_documento_financeiro_patterns
)
