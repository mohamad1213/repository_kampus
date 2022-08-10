from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('results/', views.artists_view, name='page_result'),
    path('detail/', views.detail, name='page_result'),
]
