# music_db/urls.py

# description: direct URL requests to view functions

from django.urls import path
from .views import *

#-----------------------------------

urlpatterns =[
    path('', ShowAllAlbumsView.as_view(), name="show_all_albums"),
    path('home', ShowAllAlbumsView.as_view(), name="home"),    
]