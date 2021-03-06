from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random

#####################################################################
class Son( models.Model ):
    '''
        Defines the informations about a video displayed on the site.
    '''
    # choice vars 
    video_source_choices = (
        ('youtube', 'youtube'),
        ('soundcloud', 'soundcloud'),
        ('vimeo', 'vimeo'),
        ('other', 'iframe'),
    )
    # attributes
    uid = models.AutoField(
        primary_key = True , 
        db_index = True)
    title = models.CharField(
        'Titre',
        max_length = 255)
    source_site = models.CharField(
        'Plateforme source',
        max_length = 50, 
        choices = video_source_choices)
    source_url = models.CharField(
        'URL complète du son',
        max_length = 200)
    source_id_string = models.CharField(
        'Caractères uniques du son',
        max_length = 100)
    thumbnail = models.ImageField(
        'Image d\'aperçu',
        upload_to = 'static/main/img')
    audio_file = models.FileField(
        'Fichier son',
        upload_to = 'static/main/audio',
        null = True,
        blank = True)
    tags = models.ManyToManyField(
        'Tag', 
        related_name = 'video_tags', 
        blank = True)
    is_visible = models.BooleanField(
        'Visible dès maintenant?',
        default = False)
    created_date = models.DateField(
        'A quelle date le rendre visible',
        default = timezone.now)
    modified_date = models.DateTimeField(
        auto_now = True)
    short_desc = models.CharField(
        'Un petit mot facultatif',
        max_length = 72, 
        blank = True, 
        null = True)
    posted_by = models.ForeignKey(
        User, 
        models.SET_NULL, 
        blank = True, 
        null = True,
        related_name = 'son_author')
    # Methods
    def __str__(self):
        return str(self.title)
    def colorbox_link(self):
        if self.source_site == 'soundcloud':
            complete_link = '/soundcloud_iframe/{}'.format(
                self.source_id_string)
        elif self.source_site == 'youtube':
            complete_link = '/youtube_iframe/{}'.format(
                self.source_id_string)
        elif self.source_site == 'vimeo':
            complete_link = '/vimeo_iframe/{}'.format(
                self.source_id_string)
        return complete_link
        

#####################################################################
class Tag( models.Model ):
    '''
        Each Son has tags, which are used to compile playlists
    '''
    category_choices = (
        ( 1 , 'Style de musique' ) , 
        ( 2 , 'Type de performance' ) , 
        ( 3 , 'Ambiance') , )
    class Meta:
        ordering = ['title']
    uid = models.AutoField(
        primary_key = True,
        db_index = True)
    title = models.CharField(
        max_length = 100,
        unique = True)
    category = models.PositiveIntegerField(
        choices = category_choices )
    # Methods
    def __str__(self):
        return str(self.title)
    def tag_son_count(self):
        sons_tagged = [i for i in Son.objects.filter(tags = self.uid)]
        sons_tagged_count = len(sons_tagged)
        return sons_tagged_count
    def random_son(self):
        random_son = Son.objects.filter(tags = self).order_by('?').first()
        return random_son


#####################################################################
class Subscriber( models.Model ):
    """
        To collect email addresses for the newsletter
    """
    uid = models.AutoField(
        primary_key = True,
        db_index = True)
    name = models.CharField(
        'Votre nom ou pseudonyme — facultatif',
        null = True,
        blank= True,
        max_length = 50)
    email = models.CharField(
        'Votre email',
        max_length = 100,
        unique = True)
    forum_user = models.BooleanField(
        'Voulez vous être aussi inscrit au forum ?',
        default = False)
    created_date = models.DateField(
        'Date de création',
        default = timezone.now)
    modified_date = models.DateTimeField(
        auto_now = True)