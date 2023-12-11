from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('musician/', include('musicain.urls')),  # URL configuration for the musician app
    path('album/', include('allbum.urls')),        # URL configuration for the album app
       # URL configuration for the album app
    # other app URLs...
]
