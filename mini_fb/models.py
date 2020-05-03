from django.db import models
from django.urls import reverse

# Create your models here.


class Profile(models.Model):
    '''Profile for a a person '''
    firstN = models.TextField(blank=False, verbose_name="First Name")
    lastN = models.TextField(blank=False, verbose_name="Last Name")
    city = models.TextField(blank=False, verbose_name="City")
    email = models.TextField(blank=False, verbose_name="Email Adress")
    image_url = models.URLField(blank=True, verbose_name="Image URL")

    def __str__(self):
        return '%s %s' % (self.firstN, self.lastN)

    def get_status_message(self):
        '''return a QuerySet of all status messages for this person.'''

        statuses = StatusMessage.objects.filter(profile=self.pk)
        return statuses

    def get_absolute_url(self):
        '''Return a URL to the profile'''
        return reverse("show_profile_page", kwargs={"pk":self.pk})


class StatusMessage(models.Model):
    ''' Facebook status messages'''
    timestamp = models.TimeField(blank=False)
    message = models.TextField(blank=False)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def get_time(self):
        return self.timestamp

