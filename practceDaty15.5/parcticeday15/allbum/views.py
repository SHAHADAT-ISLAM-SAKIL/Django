from django.shortcuts import render, get_object_or_404
from .models import Album
from .forms import AlbumForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
from .forms import AlbumForm

def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            return redirect('musician_detail', pk=album.musician.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album_edit.html', {'form': form})

def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    musician_pk = album.musician.pk
    if request.method == 'POST':
        album.delete()
        return redirect('musician_detail', pk=musician_pk)
    return render(request, 'album_delete.html', {'album': album})