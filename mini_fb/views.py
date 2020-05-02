from django.shortcuts import render

from django.views.generic import ListView
from .models import Profile

# Create your views here.

class ShowAllProfilesView(ListView):
    '''Create a view to show all profiles'''
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html' 
    context_object_name = 'all_profiles'




