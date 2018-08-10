from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
import operator #for sorting objects from different tables in one aggregated list
from .forms import UploadSonForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from subprocess import call
from django.shortcuts import redirect
import youtube_dl
from os import chdir
import re
from .scripts import GetNextPostTime

#####################################################################
def FrontPage(request):
    '''
        Landing page for the whole blog. It has a search form which
        looks up titles, tags, article texts.
    '''
    all_tags = Tag.objects.all().order_by('title')
    # registered users get to see all sons before they're posted
    if request.user.is_authenticated:
        last_sons = [i for i in Son.objects.select_related(
            ).all().order_by(
            'created_date').reverse()]
    else:
        last_sons = [i for i in Son.objects.select_related(
            ).filter(is_visible=True).order_by(
            'created_date').reverse()]
    paginator = Paginator(last_sons, 12)
    page = request.GET.get('page')
    sons_to_display = paginator.get_page(page)
    context={
        'all_tags': all_tags,
        'sons_to_display': sons_to_display,
        'player_enabled' : False,
        'colorbox_enabled' : True,
    }
    template = loader.get_template('main/frontpage.html')
    return HttpResponse(template.render(context, request))

#####################################################################
def TagList(request):
    '''
        Landing page for the whole blog. It has a search form which
        looks up titles, tags, article texts.
    '''
    all_tags = Tag.objects.all().order_by('title')

    paginator = Paginator(all_tags, 12)
    page = request.GET.get('page')
    tags_to_display = paginator.get_page(page)
    context={
        'tags_to_display': tags_to_display,
        'player_enabled' : False,
        'colorbox_enabled' : True,
    }
    template = loader.get_template('main/taglist.html')
    return HttpResponse(template.render(context, request))

#####################################################################
def Playlist(request, tag_title):
    '''
        Displays all sons from a tag list and allows playing.
        If the special tag 'shuffle' is passed, we pick 20 random sons
        in the list and play them all.
    '''
    if tag_title == 'shuffle':
        playlist_content = Son.objects.filter(
            is_visible = True).exclude(
            source_site = 'vimeo').order_by(
            '?')[:20]
        page_title = 'Shuffle 20 !'
    else:
        tag = Tag.objects.get(title = tag_title)
        playlist_content = Son.objects.filter(
            tags = tag, is_visible = True).exclude(
            source_site = 'vimeo')
        page_title = tag.title

    context={
        'playlist_content': playlist_content,
        'page_title': page_title,
        'player_enabled' : True,
        'colorbox_enabled' : False,
    }
    template = loader.get_template('main/playlist.html')
    return HttpResponse(template.render(context, request))

#####################################################################
def ClipList(request):
    '''
        Landing page for the whole blog. It has a search form which
        looks up titles, tags, article texts.
    '''
    all_clips = Son.objects.filter(
        tags__title = 'Super-Clip', is_visible = True).order_by(
        'created_date').reverse()

    paginator = Paginator(all_clips, 12)
    page = request.GET.get('page')
    clips_to_display = paginator.get_page(page)
    context={
        'clips_to_display': clips_to_display,
        'player_enabled' : False,
        'colorbox_enabled' : True,
    }
    template = loader.get_template('main/clip_list.html')
    return HttpResponse(template.render(context, request))

#####################################################################
def UploadSon(request):
    '''
        Tool to upload a son and get the corresponding mp3
    '''
    if request.user.is_staff:
        if request.method == 'GET':
            context = {
                'upload_son_form': UploadSonForm(),
            }
            template = loader.get_template('main/upload_son.html')
            return HttpResponse(template.render(context, request))
        elif request.method == "POST":
            form = UploadSonForm(request.POST, request.FILES)
            if form.is_valid():
                new_son = Son()
                new_son.title = form.cleaned_data['title']
                new_son.source_site = form.cleaned_data['source_site']
                new_son.thumbnail = form.cleaned_data['thumbnail']
                new_son.source_id_string = form.cleaned_data['source_id_string']
                new_son.source_url = form.cleaned_data['source_url']
                # after the audio is DLd from the source site
                # we rename the file as its source_id_string
                new_son.audio_file = 'static/main/audio/{}-{}.mp3'.format(
                    form.cleaned_data['title'], form.cleaned_data['source_id_string'])
                new_son.is_visible = False
                new_son.created_date = GetNextPostTime()
                new_son.short_desc = form.cleaned_data['short_desc']
                new_son.posted_by = form.cleaned_data['posted_by']
                new_son.save()
                if form.cleaned_data['tags']:
                    for tag in form.cleaned_data['tags']:
                        new_son.tags.add(tag)
                else:
                    pass
                # we DL the mp3
                if new_son.source_site == "youtube":
                    chdir('/home/common/sonov_django/static/main/audio')
                    ydl_opts = {
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '320',
                        }],
                    }
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([form.cleaned_data['source_url'],])
                elif new_son.source_site == "soundcloud":
                    son_to_dl = scdl.get_item(form.cleaned_data['source_url'])
                    os.chdir('/home/common/sonov_django/static/main/audio')
                    scdl.download_track(item)
                return HttpResponseRedirect('/')                        
            else:
                context = {
                    'upload_son_form': UploadSonForm(),
                    'errors' : [i for i in form.errors],
                    'player_enabled' : False,
                    'colorbox_enabled' : False,
                }
                template = loader.get_template('main/upload_son.html')
                return HttpResponse(template.render(context, request))
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


#####################################################################
def SoundcloudIframe(request, soundcloud_id):
    '''
        Test for embedding soundcloud within colorbox
    '''
    context={
        'soundcloud_id': soundcloud_id,
    }
    template = loader.get_template('main/soundcloud_iframe.html')
    return HttpResponse(template.render(context, request))

#####################################################################
def YoutubeIframe(request, youtube_id):
    '''
        Test for embedding soundcloud within colorbox
    '''
    context={
        'youtube_id': youtube_id,
    }
    template = loader.get_template('main/youtube_iframe.html')
    return HttpResponse(template.render(context, request))

#####################################################################
def VimeoIframe(request, vimeo_id):
    '''
        Test for embedding soundcloud within colorbox
    '''
    context={
        'vimeo_id': vimeo_id,
    }
    template = loader.get_template('main/vimeo_iframe.html')
    return HttpResponse(template.render(context, request))