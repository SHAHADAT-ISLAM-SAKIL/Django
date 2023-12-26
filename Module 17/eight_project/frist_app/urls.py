from django.urls import path 
from . import views
urlpatterns = [
    path('', views.base, name = 'homepage'),
    path('singup/', views.singup, name = 'singup'),
    path('profile/', views.profile, name = 'profile'),
    path('login/', views.user_login, name = 'login'),
    path('passchange/', views.passchange, name = 'passchange'),
    path('passchange2/', views.passchange2, name = 'passchange2'),
    path('logout/', views.user_logout, name = 'logout'),
    # path('change_user_data/', views.change_user_data, name = 'change_user_data'),

]

