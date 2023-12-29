from django.urls import path,include
from . import views
urlpatterns = [
  
   
    path('add/',views.add_Musician, name = 'musician'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name ='logout'),
    path('edit/<int:id>',views.edit_Musician,name='edit_musician'),
    path('delete/<int:id>',views.delete_musician,name='delete_musician'),

]