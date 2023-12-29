from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name= 'home'),
    path('musician/',include ('musician_app.urls')),
    path('album/',include('album_app.urls'))
]