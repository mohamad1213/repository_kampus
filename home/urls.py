from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('results/', views.artists_view, name='page_result'),
    path('results/<pk>/detail/', views.detail, name='detail'),
    path('results/<pk>/post_favorite/', views.post_favorite, name='fav'),
    path('results/<pk>/post_favorite_kartul/', views.post_favorite_kartul, name='fav2'),
    path('list_fav/', views.list_fav, name='list_fav'),
    path('profile/', views.AccountsSettings, name="profile"),


] 