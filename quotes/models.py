from django.db import models
from django.urls import reverse
import random

# Create your models here.

class Person(models.Model):
    '''Encapsulate the concept of a person, who said some famous quote.'''

    name = models.TextField(blank=False)

    def __str__(self):
        '''Return a string representation of this Person.'''
        return self.name

    def get_random_image(self):
        '''Return a random Image of the person'''

        #get all images of this person
        images = Image.objects.filter(person=(self.pk))

        #then, pick one at random and return it
        i = random.randint(0, len(images) -1)
        return images[i]

    #get all images for this person
    def get_all_images(self):
        '''return a QuerySet of all images for this person.'''

        images = Image.objects.filter(person=self.pk)
        return images

    #get all quotes for this person
    def get_all_quotes(self):
        '''return a QuerySet of all images for this person.'''

        quotes = Quote.objects.filter(person=self.pk)
        return quotes



class Quote(models.Model):
    '''Encapsulate the idea of a quote (i.e., text),'''

    # data attributes of a quote:
    text = models.TextField(blank=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        '''Returns a string representation of this object.'''
        return '"{{%s" - %s}}' % (self.text, self.person.name)

    def get_absolute_url(self): 
        '''Return a URL to display this quote object.'''
        return reverse("quote", kwargs={"pk":self.pk})



class Image(models.Model):
    '''Represent an image, which is associated with a Person.'''

    image_url = models.URLField(blank=True)
    image_file = models.ImageField(blank=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        '''Return a string representation of this image.'''
        if self.image_url:
            return self.image_url
        else:
            return self.image_file.url