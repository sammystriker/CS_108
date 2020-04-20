from django.shortcuts import render

# Create your views here.
from .models import Quote
from django.views.generic import ListView

class HomePageView(ListView):
    '''Create a suclass of ListView to display all quotes,'''

    model = Quote # retrieve objects of Type Quote from the database
    template_name = 'quotes/home.html'
    context_object_name = 'all_quotes_list' # how to find the data in the template file