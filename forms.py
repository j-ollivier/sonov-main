from django import forms
from .models import *
from django.forms import ModelForm

class UploadSonForm(ModelForm):
    class Meta:
        model = Son
        fields= ['title','source_site', 'source_url', 
        'thumbnail','tags', 'short_desc','posted_by']