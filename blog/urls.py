from django.urls import path
from . import views

urlpatterns = [
    path('', views.glowna, name='glowna'),
    path('wpis/<int:pk>/', views.wpis_wpis, name='wpis_wpis'),
]
