# quotes/forms.py

from django import forms
from .models import Quote, Image

class CreateQuoteForm(forms.ModelForm):
    ''' A form to add new quotes to the database.'''

    class Meta:
        '''associate thos form with the Quote model.'''
        model = Quote
        fields = ['person','text'] #which fields from model should we use


class UpdateQuoteForm(forms.ModelForm):
    '''A form to update a quote to the database.'''

    class Meta:
        '''associate thos form with the Quote model.'''
        model = Quote
        fields = ['person','text'] #which fields from model should we use

class AddImageForm(forms.ModelForm):
    '''A form to collect an image from the user.'''

    class Meta:
        model = Image
        fields = ["image_file",]
