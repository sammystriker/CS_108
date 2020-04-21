from django.shortcuts import render

# Create your views here.
from .models import Quote
from django.views.generic import ListView, DetailView
import random

class HomePageView(ListView):
    '''Create a suclass of ListView to display all quotes,'''

    model = Quote # retrieve objects of Type Quote from the database
    template_name = 'quotes/home.html'
    context_object_name = 'all_quotes_list' # how to find the data in the template file

class QuotePageView(DetailView):
    '''Show the details for one quote.'''
    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

class RandomPageView(DetailView):
    '''Show the details of one random quote'''


    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name ='quote'

    #pick one quote at random 
    def get_object(self):
        '''Return a single instance of a Quote object, selected at random'''

        #get all quotes
        all_quotes = Quote.objects.all()

        #pick one, at random
        r = random.randint(0, len(all_quotes) -1)
        q = all_quotes[r]
        return q # return this object
