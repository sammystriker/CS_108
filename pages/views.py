from django.shortcuts import render
from django.views.generic import TemplateView



# Create your views here.
class HomePageView(TemplateView): 
    '''A speeacialized version of TemplateView to display our home page.'''

    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    '''A speeacialized version of TemplateView to display our about page.'''

    template_name= "pages/about.html"


class SchedulePageView(TemplateView):
    '''A speeacialized version of TemplateView to display our schedule page.'''

    template_name= "pages/schedule.html"