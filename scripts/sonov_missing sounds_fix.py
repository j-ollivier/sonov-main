# python 3.6.3
# We try to fix the missing mp3 from the library to have a perfect playlist tool.
# This script is meant to be executed through django's shell

from main.models import Son
import youtube_dl
from os import chdir , path

sons = Son.objects.filter( source_url__in = [ None , ''] , source_site = 'youtube' )
for son in sons:
    son.source_url = 'https://www.youtube.com/watch?v={}'.format( son.source_id_string )
    son.save()