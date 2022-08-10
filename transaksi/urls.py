from django.urls import path

from . import views
urlpatterns = [
    path('', views.transaksi, name = 'transaksi'),
    path('<str:id>/detail/', views.detail_transaksi),
    path('<id>/delete/', views.delete_transaksi),
    path('<id>/update/', views.update_transaksi),
]
