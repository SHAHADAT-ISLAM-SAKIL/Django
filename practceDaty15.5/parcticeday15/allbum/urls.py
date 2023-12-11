from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/edit/', views.album_edit, name='album_edit'),
    path('<int:pk>/delete/', views.album_delete, name='album_delete'),
    # other album-related URLs...
]
