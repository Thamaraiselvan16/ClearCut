from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('remback/', views.remback, name='remback'),
    path('download/<str:filename>/', views.download, name='download'),
]
