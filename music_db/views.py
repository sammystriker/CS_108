from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from .models import Album, Artist, Song

class ShowAllAlbumsView(ListView):
    '''Create a view to show all profiles'''
    model = Album
    template_name = 'music_db/show_all_album_view.html' 
    context_object_name = 'all_albums'

class ShowAlbumPageView(DetailView):
    '''create a view to show one album'''
    model= Album
    template_name = 'music_db/show_all_albums.html'
    context_object_name = 'album' 
