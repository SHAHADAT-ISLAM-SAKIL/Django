from django.shortcuts import render, get_object_or_404, redirect
from .models import Musician
from .forms import MusicianForm

def musician_list(request):
    musicians = Musician.objects.all()
    return render(request, 'musician_list.html', {'musicians': musicians})

def musician_detail(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    return render(request, 'musician_detail.html', {'musician': musician})

def musician_new(request):
    if request.method == "POST":
        form = MusicianForm(request.POST)
        if form.is_valid():
            musician = form.save(commit=False)
            musician.save()
            return redirect('musician_detail', pk=musician.pk)
    else:
        form = MusicianForm()
    return render(request, 'musician_edit.html', {'form': form})

def musician_edit(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    if request.method == "POST":
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            musician = form.save(commit=False)
            musician.save()
            return redirect('musician_detail', pk=musician.pk)
    else:
        form = MusicianForm(instance=musician)
    return render(request, 'musician_edit.html', {'form': form})

def musician_delete(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    if request.method == 'POST':
        musician.delete()
        return redirect('musician_list')
    return render(request, 'musician_confirm_delete.html', {'musician': musician})
