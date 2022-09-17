from django.urls import path

from admin1.views import ProfileView
app_name = 'administration'

from . import views
urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', views.index, name='admin'),
    # path('profile/', views.profile, name="profile"),
    path('profile/edit/<pk>/', views.accountSettings, name="profile-edit"),
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
