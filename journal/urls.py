from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('entries/', views.all_entries, name='all_entries'),
    path('entries/<int:pk>/', views.entry_detail, name='entry_detail'),
]

