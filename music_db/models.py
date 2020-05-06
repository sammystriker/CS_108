from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.TextField(blank = False)
    bio = models.TextField(blank = True)
    hometown = models.TextField(blank=False, verbose_name="Hometown")
    birthday = models.DateField(blank = False)
    propic = models.ImageField(blank=True)

    def __str__(self):
        return self.name

class Album(models.Model): 
    GOLD = 'Gold'
    PLATINUM =  'Platinum'
    MUlTI_PLAT =  'Multi-Platinum'
    DIAMOND =  'Diamond'
    NONE =  'None'
    certs = [
        (GOLD, 'Gold'),
        (PLATINUM, 'Platinum'),
        (MUlTI_PLAT, 'Multi-Platinum'),
        (DIAMOND, 'Diamond'),
        (NONE, 'None')
    ]

    album_name = models.TextField(blank=False, verbose_name="Album Name")
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    cover = models.ImageField(blank=False)
    RIAAcerts = models.TextField(choices=certs, default=None)
    release_date = models.DateField(blank = False, verbose_name = "Release Date")
    genre = models.TextField(blank=False)

    def __str__(self):
        '''returns name of an album'''
        return self.album_name

    def get_artist_name(self):
        '''returns the artist of an album'''
        a = Artist.objects.get(pk=self.artist.pk)
      
        return a.name

     
    

class Song(models.Model):
    album = models.ForeignKey('Album', on_delete = models.CASCADE)
    name = models.TextField(blank = False)
    track_number = models.SmallIntegerField(blank=False)
    features = models.ManyToManyField('Artist', blank = True)
    
    def __str__(self):
        return self.name


