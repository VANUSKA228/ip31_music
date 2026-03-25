from django.shortcuts import render, redirect
from .models import Genre,Track
from .form import GenreForm, TrackForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def genres_page(request):
    genres = Genre.objects.all()
    return render(request, 'genres.html', {'genres': genres})

# добавить жанр
def addgenre(request):
    if request.method == "POST":
        form = GenreForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('/genres')
    else:
        form = GenreForm() 
    
    return render(request, "addgenre.html", {'form': form})

def editgenre(request, id):
    g = Genre.objects.get(id=id)
    if request.method == "POST":
        form = GenreForm(request.POST, instance=g)
        if form.is_valid():
            form.save()
            return redirect('/genres')
    else:
        form = GenreForm(instance=g)
    return render(request, "addgenre.html", {'form': form})
            

def dellgenre(request, id):
    genre = Genre.objects.get(id=id)
    genre.delete()
    return redirect('/genres') 

def tracks_page(request):
    tracks = Track.objects.all()
    return render(request, 'tracks.html', {'tracks': tracks})

def add_track(request):
    if request.method == "POST":
        form = TrackForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('/tracks')
    else:
        form = TrackForm() 
    
    return render(request, "add_track.html", {'form': form})

def delltracks(request, id):
    tracks = Track.objects.get(id=id)
    tracks.delete()
    return redirect('/tracks') 



def edit_tracks(request, id):
    g = Track.objects.get(id=id)
    if request.method == "POST":
        form = TrackForm(request.POST, instance=g)
        if form.is_valid():
            form.save()
            return redirect('/tracks')
    else:
        form = TrackForm(instance=g)
    return render(request, "add_track.html", {'form': form})