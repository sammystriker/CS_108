from django.db import models
from django.urls import reverse

# Create your models here.


class Profile(models.Model):
    '''Profile for a person '''
    firstN = models.TextField(blank=False, verbose_name="First Name")
    lastN = models.TextField(blank=False, verbose_name="Last Name")
    city = models.TextField(blank=False, verbose_name="City")
    email = models.TextField(blank=False, verbose_name="Email Adress")
    image_url = models.URLField(blank=True, verbose_name="Image URL")
    friends = models.ManyToManyField("self", blank=True)

    def get_pk(self):
        return self.pk

    def __str__(self):
        return '%s %s' % (self.firstN, self.lastN)

    def get_status_message(self):
        '''return a QuerySet of all status messages for this person.'''

        statuses = StatusMessage.objects.filter(profile=self.pk)
        return statuses

    def get_absolute_url(self):
        '''Return a URL to the profile'''
        return reverse("show_profile_page", kwargs={"pk":self.pk})

    def get_friends(self):
        '''return a QuerySet of all of this person's friends.'''
        friend_set = self.friends.all()
        return friend_set

    def get_news_feed(self):
        '''returns statuses of friends only'''
        news = StatusMessage.objects.filter(profile__in=(self.get_friends())).order_by("-timestamp")
        return news

    def get_friend_suggestions(self):
        '''returns the list of people this person is not friends with'''
        
        current_friends = self.get_friends()
        friend_suggestions = Profile.objects.exclude(pk = self.pk)
        fs2 = friend_suggestions.exclude(pk__in=current_friends)
        #for fr in current_friends:
        #    fs2 = friend_suggestions.objects.exclude(pk__in=)
        

        return fs2




class StatusMessage(models.Model):
    ''' Facebook status messages'''
    timestamp = models.TimeField(blank=False)
    message = models.TextField(blank=False)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.message

    def get_time(self):
        return self.timestamp

