from django.urls import path
from . import views

urlpatterns = [
    path('', views.musician_list, name='musician_list'),
    path('details/<int:pk>/', views.musician_detail, name='musician_detail'),
    path('new/', views.musician_new, name='musician_new'),
    path('<int:pk>/edit/', views.musician_edit, name='musician_edit'),
    path('<int:pk>/delete/', views.musician_delete, name='musician_delete'),
]
