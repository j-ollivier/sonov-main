# python 3.6.3
# We try to fix the missing mp3 from the library to have a perfect playlist tool.
# This script is meant to be executed through django's shell

from main.models import Son
import youtube_dl
from os import chdir , path

son_list = ['-WoP-jtTBH0' ,'335Ze_N_ei0' ,'3NPxqXMZq7o' ,'4PDEyrk22mk' ,'6KsqpNMqn9o' ,'8CeVUK6dIw0' ,'AJx6PPqWs50' ,'awPo_VZabRc' ,'b80DqcFLI-c' ,'YZKFN9jK2uU' ,'EWES7Uqbc9A' ,'EZ_90dlt4JI' ,'Gt06Lkv6eaM' ,'he-ftMfWORI' ,'kTn0li1q1O0' ,'mDIjYoB-hKY' ,'nSrDr9qXlVk' ,'rgpeZehATH4' ,'RLZhQ_ugeGY' ,'roGmGWOOcTA' ,'rWxtvGYwgwc' ,'sdl7PZmlGQI' ,'VHlOzCQDZzg' ,'wwZbonjAlPc' ,'WzDXsmW3p1w' ,'y5F05K07kfE' ,'yrfYst1H2G4' ,'Zs27PEFzEv8' ,]

sons = Son.objects.filter( source_id_string__in = son_list )
for son in sons:
    son.audio_file = 'static/main/audio/{}.mp3'.format( son.source_id_string )
    son.save()