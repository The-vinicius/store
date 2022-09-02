from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from products.views import CategoryView, CategoryProductView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorias/', CategoryView.as_view(), name='category'),
    path('categorias/<slug:slug>/', CategoryProductView.as_view(), name='category_list'),
    path('produtos/', include('products.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
