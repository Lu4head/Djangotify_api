from django.contrib import admin
from genres.models import Genre

admin.site.site_header = 'Djangotify Admin'
admin.site.site_title = 'Djangotify Admin Area'
admin.site.index_title = 'Welcome to the Djangotify Admin Area'

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['name']
    ordering = ['name']