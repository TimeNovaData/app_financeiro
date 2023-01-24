from .rateio_create import RateioCreateView
from .rateio_delete import RateioDeleteView
from .rateio_detail import RateioDetailView
from .rateio_list import RateioListView
from .rateio_update import RateioUpdateView

__all__ = [
    RateioListView,
    RateioDeleteView,
    RateioDetailView,
    RateioCreateView,
    RateioUpdateView,
]
