from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random

#####################################################################
class Son(models.Model):
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
        max_length = 255)
    source_site = models.CharField(
        max_length = 50, 
        choices = video_source_choices)
    source_url = models.CharField(
        max_length = 200)
    source_id_string = models.CharField(
        max_length = 100)
    thumbnail = models.ImageField(
        upload_to = 'static/main/thumbnail')
    audio_file = models.FileField(
        upload_to = 'static/main/audio',
        null = True,
        blank = True)
    tags = models.ManyToManyField(
        'Tag', 
        related_name = 'video_tags', 
        blank = True)
    is_visible = models.BooleanField(
        default = False)
    created_date = models.DateTimeField(
        default = timezone.now)
    modified_date = models.DateTimeField(
        auto_now = True)
    short_desc = models.CharField(
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
class Tag(models.Model):
    '''
        Each Son has tags, which are used to compile playlists
    '''
    uid = models.AutoField(
        primary_key = True,
        db_index = True)
    title = models.CharField(
        max_length = 100,
        unique = True)
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

