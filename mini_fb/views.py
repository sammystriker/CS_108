from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Profile

# Create your views here.

class ShowAllProfilesView(ListView):
    '''Create a view to show all profiles'''
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html' 
    context_object_name = 'all_profiles'


class ShowProfilePageView(DetailView):
    '''Create a view to show one profiles'''
    model = Profile
    template_name = 'mini_fb/show_profile_page.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        '''Return a dictionary with context data for this template to use.'''

        #get the default context data:
        #this will include the Person record for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)

        #return the context dictionary
        return context


