from django.contrib import admin
from .models import *
# Register your models here.
class AdminSon(admin.ModelAdmin):
    list_display =['uid', 'source_site','is_visible', 'title','created_date', 'modified_date', 'posted_by']
    ordering = ['-created_date']
admin.site.register(Son, AdminSon)

class AdminTag(admin.ModelAdmin):
    list_display =['uid','title','category']
    ordering = ['uid']
admin.site.register(Tag, AdminTag)