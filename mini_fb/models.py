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
