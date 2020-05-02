from django.db import models

# Create your models here.


class Profile(models.Model):
    '''Profile for a a person '''
    firstN = models.TextField(blank=False)
    lastN = models.TextField(blank=False)
    city = models.TextField(blank=False)
    email = models.TextField(blank=False)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return '%s %s' % (self.firstN, self.lastN)

    def get_status_message(self):
        '''return a QuerySet of all status messages for this person.'''

        statuses = StatusMessage.objects.filter(profile=self.pk)
        return statuses


class StatusMessage(models.Model):
    ''' Facebook status messages'''
    timestamp = models.TimeField(blank=False)
    message = models.TextField(blank=False)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def get_time(self):
        return self.timestamp

