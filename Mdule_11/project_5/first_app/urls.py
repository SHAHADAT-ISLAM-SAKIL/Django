from django.urls import path 
from . import views
urlpatterns = [
    path('', views.index , name = 'home'),
    path('about/', views.about, name = 'about'),
    path('from/', views.submit_form, name = 'from'),
    path('django_from/', views.PassowardValidation, name = 'django_from'),
 
]