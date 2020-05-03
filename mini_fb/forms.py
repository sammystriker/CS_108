from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    ''' A form for creating a profile ''' 
    firstN = forms.CharField(label="First Name", required=True)
    lastN = forms.CharField(label="Last Name", required=True)
    city = forms.CharField(label="City", required=True)
    email = forms.CharField(label="Email Address", required=True)
    image_url = forms.URLField(label="Image URL", required=True)

    class Meta:
        model= Profile
        fields = ['firstN','lastN','city','email','image_url']


class UpdateProfileForm(forms.ModelForm):

    city = forms.CharField(label="City", required=True)
    email = forms.CharField(label="Email Address", required=True)
    image_url = forms.URLField(label="Image URL", required=True)

    class Meta:
        model= Profile
        fields = ['city','email','image_url']

class CreateStatusMessageForm(forms.ModelForm):
    message = forms.Textarea()
    image = forms.ImageField(required=False)

    class Meta:
        model= StatusMessage
        fields = ['message','image']