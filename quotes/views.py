from django.shortcuts import render


# Create your views here.
from .models import Quote, Person
from django.views.generic import ListView, DetailView
import random
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from django.urls import reverse
from django.shortcuts import redirect

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


class PersonPageView(DetailView):
    '''Show all quotes and all images for one person.'''

    model = Person
    template_name = 'quotes/person.html'
    #context_object_name = 'person'

    def get_context_data(self, **kwargs):
        '''Return a dictionary with context data for thos template ro use.'''

        #get the default context data:
        #this will include the Person record for this page view
        context = super(PersonPageView, self).get_context_data(**kwargs)

        #create the add image form:
        add_image_form = AddImageForm()
        context['add_image_form'] = add_image_form

        #return the context dictionary
        return context



class CreateQuoteView(CreateView):
    '''A view to create a new quote and save it to the database.'''

    form_class = CreateQuoteForm
    template_name = "quotes/create_quote.html"

class UpdateQuoteView(UpdateView):
    '''A view to create a new quote and save it to the database.'''

    form_class = UpdateQuoteForm
    template_name = "quotes/update_quote.html"
    queryset = Quote.objects.all()

class DeleteQuoteView(DeleteView):
    '''A view to create a new quote and save it to the database.'''

    template_name = "quotes/delete_quote.html"
    queryset = Quote.objects.all()

    def get_success_url(self):
        '''Return the url to redirect to aftdre a deletion.'''

        #get the pk for this quote
        pk = self.kwargs.get('pk')
        quote = Quote.objects.filter(pk=pk).first()

        #find the person assiciated with the quote
        person = quote.person
        return reverse('person', kwargs={'pk':person.pk})


def add_image(request, pk):
    '''A Custom vieew function to handle the subission of a image uplaod.'''

    #find the person for whom we submitting the image
    person = Person.objects.get(pk=pk)

    #read request data into AddImageForm object
    form = AddImageForm(request.POST or None, request.FILES or None)
    
    # check if the form is valid, save obkect to database
    if form.is_valid():

        image = form.save(commit=False) # create the image object, but not save
        image.person = person
        image.save()
    else:
        print("Error: the form was not valid.")
    #redirect to a new URL, display person page
    url = reverse('person', kwargs={'pk':pk})
    return redirect(url)