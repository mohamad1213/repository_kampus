from django.urls import path
app_name = 'administration'

from . import views
urlpatterns = [
    path('', views.index, name='admin'),
    path('profile/', views.AccountsSettings, name="profile"),
    path('mhs/', views.ListMhs, name='mhs'),
    path('mhs/<pk>/', views.DetailMhs, name='detail_mhs'),
    path('journal/', views.ListJournal, name='journal'),
    path('journal/create/', views.CreateJournal, name='create_journal'),
    path('journal/detail/<pk>/', views.DetailJournal, name='detail_journal'),
    path('journal/update/<pk>/', views.UpdateJournal, name='update_journal'),
    path('journal/delete/<pk>/', views.DeleteJournal, name='delete_journal'),
    path('skripsi/', views.ListSkripsi, name='skripsi'),
    path('skripsi/create/', views.CreateSkrispi, name='create_skripsi'),
    path('skripsi/update/<pk>/', views.UpdateSkripsi, name='update_skripsi'),
    path('skripsi/delete/<pk>/', views.DeleteSkrispi, name='delete_skripsi'),
    path('skripsi/detail/<pk>/', views.DetailSkripsi, name='detail_skripsi'),
] 
