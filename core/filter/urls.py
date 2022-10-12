from django.urls import path
from .views import FilterProductView

app_name = "filter"

urlpatterns = [
    path(
        "<slug:slug>_mais<int:price_gt>_menos<int:price_lt>/",
        FilterProductView.as_view(),
        name="result",
    ),
]
