from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('administration/', include('admin1.urls')),
    # path('barang/', include('barang.urls')),
    # path('category/', include('barang.urls_cat')),
    # path('transaksi/', include('transaksi.urls')),
    path('accounts/', include('account.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)