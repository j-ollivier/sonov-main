from django import forms
from .models import *
from django.forms import ModelForm

class UploadSonForm(ModelForm):
    class Meta:
        model = Son
        fields= ['title','source_site', 'source_url', 
        'source_id_string','thumbnail','tags', 'short_desc','posted_by']