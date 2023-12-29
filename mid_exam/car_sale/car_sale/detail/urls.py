from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   
    # path('detail/',views.add_car,name='detail'),
    path("detail/",views.AddCarCreateView.as_view(),name = 'detail'),
    path("view/<int:id>/",views.CarDetailView.as_view(),name = 'view_all'),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)