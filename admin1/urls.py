from django.urls import path


app_name = 'administration'
from . import views
urlpatterns = [
    path('', views.index, name='admin'),
    path('profile/', views.profile, name="profile"),
    path('profile/<pk>/edit', views.accountSettings, name="profile-edit"),
    path('karya_tulis/', views.karya_tulis, name='karya_tulis'),
    path('karya_tulis/<pk>/detail/', views.detail_karya_tulis, name='detail_karya_tulis'),
    path('karya_tulis/<pk>/update/', views.update_karya_tulis, name='update_karya_tulis'),
    path('karya_tulis/<pk>/delete/', views.delete_karya_tulis, name='delete_karya_tulis'),
    path('skripsi/', views.skripsi, name='skripsi'),
    path('skripsi/<pk>/update/', views.update_skripsi, name='update_skripsi'),
    path('skripsi/<pk>/delete/', views.delete_skripsi, name='delete_skripsi'),
    path('skripsi/<pk>/detail/', views.detail_skripsi, name='detail_skripsi'),
]
