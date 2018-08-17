from .models import Son
from datetime import datetime, timedelta
import re

def GetNextPostTime():
	'''
	To determine at which date the next Son object has to be made public,
	we get the last son uploaded and add 2 days. Returns a datetime.
	'''
	last_son = Son.objects.last()
	post_date = last_son.created_date + timedelta( days = 2 )
	return post_date

def ChangePostTime():
	'''
	one shot script to set all Son instances post time to midnight.
	'''
	sons = Son.objects.all()
	for son in sons : 
		son.created_date.replace( hour = 00, minute = 00, second = 00 )
		son.save()

# source : https://gist.github.com/silentsokolov/f5981f314bc006c82a41
def GetYoutubeID(youtube_url):
	'''
	Extract the youtube ID from the whole url.
	'''
	regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})')
	match = regex.match(youtube_url)
	if not match:
		return False
	else:
		return match.group('id')