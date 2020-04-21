# quotes/urls.py

# description: direct URL requests to view functions

from django.urls import path
from .views import HomePageView, QuotePageView, RandomPageView

#-----------------------------------

urlpatterns =[
    path('', RandomPageView.as_view(), name="random"),
    path('all', HomePageView.as_view(), name='home'),
    path('quote/<int:pk>',  QuotePageView.as_view(), name='quote'),

] 