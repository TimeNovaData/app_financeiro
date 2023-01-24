from .caixa_banco import (
    CaixaBancoCreate,
    CaixaBancoDelete,
    CaixaBancoDetail,
    CaixaBancoListView,
    CaixaBancoUpdate,
    caixa_banco_columns,
)
from .conta_nivel1 import (
    ContaNivel1Create,
    ContaNivel1Delete,
    ContaNivel1ListView,
    ContaNivel1Update,
    conta_nivel1_columns,
)
from .conta_nivel2 import (
    ContaNivel2Create,
    ContaNivel2Delete,
    ContaNivel2ListView,
    ContaNivel2Update,
    conta_nivel2_columns,
)
from .conta_nivel3 import (
    ContaNivel3Create,
    ContaNivel3Delete,
    ContaNivel3ListView,
    ContaNivel3Update,
    conta_nivel3_columns,
)
from .conta_nivel4 import (
    ContaNivel4Create,
    ContaNivel4Delete,
    ContaNivel4ListView,
    ContaNivel4Update,
)
from .fluxo_caixa import FluxoCaixaView
from .lancamento_financeiro import (
    LancamentoFinanceiroCreateView,
    LancamentoFinanceiroDeleteView,
    LancamentoFinanceiroDetailView,
    LancamentoFinanceiroListView,
    LancamentoFinanceiroUpdateView,
)
from .parcela import (
    ParcelaDeleteView,
    ParcelaDetailView,
    ParcelaListView,
    ParcelaUpdateView,
)
from .tipo_documento_financeiro import (
    TipoDocumentoFinanceiroCreateView,
    TipoDocumentoFinanceiroDeleteView,
    TipoDocumentoFinanceiroListView,
    TipoDocumentoFinanceiroUpdateView,
    tipo_documento_financeiro_columns,
)

caixa_banco_views = [
    CaixaBancoCreate,
    CaixaBancoDetail,
    CaixaBancoListView,
    CaixaBancoUpdate,
    CaixaBancoDelete,
    caixa_banco_columns,
]

conta_nivel1_views = [
    ContaNivel1Create,
    ContaNivel1Delete,
    ContaNivel1ListView,
    ContaNivel1Update,
    conta_nivel1_columns,
]

conta_nivel2_views = [
    ContaNivel2Create,
    ContaNivel2Delete,
    ContaNivel2ListView,
    ContaNivel2Update,
    conta_nivel2_columns,
]

conta_nivel3_views = [
    ContaNivel3Create,
    ContaNivel3Delete,
    ContaNivel3ListView,
    ContaNivel3Update,
    conta_nivel3_columns,
]

conta_nivel4_views = [
    ContaNivel4Create,
    ContaNivel4Delete,
    ContaNivel4ListView,
    ContaNivel4Update,
]

lancamento_financeiro_views = [
    LancamentoFinanceiroCreateView,
    LancamentoFinanceiroDeleteView,
    LancamentoFinanceiroDetailView,
    LancamentoFinanceiroListView,
    LancamentoFinanceiroUpdateView,
]

parcela_views = [
    ParcelaDeleteView,
    ParcelaDetailView,
    ParcelaListView,
    ParcelaUpdateView,
]

tipo_documento_financeiro_views = [
    tipo_documento_financeiro_columns,
    TipoDocumentoFinanceiroCreateView,
    TipoDocumentoFinanceiroDeleteView,
    TipoDocumentoFinanceiroListView,
    TipoDocumentoFinanceiroUpdateView,
]

__all__ = (
    [
        FluxoCaixaView,
    ]
    + caixa_banco_views
    + conta_nivel1_views
    + conta_nivel2_views
    + conta_nivel3_views
    + conta_nivel4_views
    + lancamento_financeiro_views
    + parcela_views
    + tipo_documento_financeiro_views
)
