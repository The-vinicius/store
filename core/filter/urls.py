from django.urls import path
from .views import FilterProductView, FilterSearchView

app_name = "filter"

urlpatterns = [
    path(
        "<slug:slug>_mais<int:price_gt>_menos<int:price_lt>/",
        FilterProductView.as_view(),
        name="result",
    ),
    path(
        "ss/<query>_mp<int:price_gt>_ml<int:price_lt>/",
        FilterSearchView.as_view(),
        name="search",
    ),
]
