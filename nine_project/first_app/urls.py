from django.urls import path
from .import views
urlpatterns = [
    # path('', views.home, name='homepage'),
    path('', views.set_session, name='homepage'),
    # path('get/', views.get_cookie, name='get_cookie'),
    path('get/', views.get_session, name='get_cookie'),
    # path('del/', views.delete_cookies, name= 'delete'),
    path('del/', views.delete_session, name= 'delete'),
]
