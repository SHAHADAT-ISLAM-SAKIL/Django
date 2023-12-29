from django.shortcuts import render

from album_app.models import AlbumInfo


def home(request):
    data = AlbumInfo.objects.all()
    return render(request, 'home.html', {'data': data})