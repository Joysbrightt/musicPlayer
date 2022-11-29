from django.contrib import admin

# Register your models here.
from music_app.models import User, Songs, Downloads


@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    date_hierarchy = 'song_released_date'
    list_display = ['song_name', 'song_artist', 'song_url']
    list_editable = ['song_id']
    search_fields = ['song_name']
    list_filter = ['song_artist', 'song_name']


@admin.register(Downloads)
class DownloadsAdmin(admin.ModelAdmin):
    date_hierarchy = 'according_to_latest_downloads'
    sorted(date_hierarchy)


admin.site.register(User)
