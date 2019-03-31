import os
from main.models import Son

sons_missing = []
os.chdir( 'home/common/sonov_django/static/main/audio' )

sons = Son.objects.all()

for son in sons:
    try:
        if os.stat( son.audio_file ).st_size > 0:
           pass
        else:
           pass
    except OSError:
        sons_missing.append( son.source_url )

with open( '/home/common/sonov_django/main/scripts/sons_missing.txt' , 'w' ) as ofi:
    for line in sons_missing:
        ofi.write( line )