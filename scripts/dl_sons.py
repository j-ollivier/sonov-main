# # python 3.6.3
# # This script is meant to dl all the mp3 from a list of urls taken from a postgres table.
# # This is script is meant to be executed in the django environment.

from main.models import Son
import os
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3'
    }]
}

# since the script crashes at each missing song, i make a list of all downloaded
# files, extract their source_id_string value, and make the script ignore them 
# when i run it again.
os.chdir('/home/common/sonov_django/static/main/audio')
dir_files = os.listdir()
dir_mp3 = [i for i in dir_files if i[-3:]=='mp3']
dir_mp3_id = [i[-15:-4] for i in dir_mp3]

sons = [i for i in Son.objects.filter(source_site = 'youtube')]
for son in sons:
    if son.source_id_string not in dir_mp3_id:
        son_url = 'https://www.youtube.com/watch?v=' + son.source_id_string
        print(son_url)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([son_url])
        son.source_url = son_url
        son.save()
    else:
        print('mp3 already downloaded. Passing.')
        pass


# Now we rename the mp3 into their unique id
# then link the dld mp3 to their database entry in django again.

all_sons = os.listdir()
for son in all_sons:
    son_id = son[-15:-4]
    os.rename(
        '{}'.format(son),
        '{}.mp3'.format(son_id),
        )

# Now that it's DLd, we chmod it so it can be played.