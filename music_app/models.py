from django.db import models


# Create your models here.

class User(models.Model):
    user_name = models.TextField(max_length=255, verbose_name="user_name")
    email = models.CharField(max_length=255, verbose_name="user_name")
    password = models.CharField(max_length=255, verbose_name="user_name")


class Songs(models.Model):
    SONGS_CATEGORY = (
        ('HIP_HOP', 'hip_hop'),
        ('BLUES', 'blues'),
        ('AFRO_POP', 'afro_pop'),
        ('R&B', 'r&b'),
        ('RAP', 'rap')
    )
    song_name = models.CharField(max_length=255, verbose_name="song_name")
    song_artist = models.CharField(max_length=255, verbose_name="song_artist")
    song_date = models.DateTimeField(max_length=255, verbose_name="song_date")
    song_url = models.CharField(max_length=255, verbose_name="song_date")


class Playlist(models.Model):
    playlist_name = models.CharField(max_length=255, verbose_name="song_name")
    User = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user")


class PlaylistTrack(models.Model):
    Playlist = models.ForeignKey("Playlist", on_delete=models.CASCADE, related_name="playlist")
    Songs = models.ForeignKey("Songs", on_delete=models.CASCADE, related_name="songs")


class Recent(models.Model):
    User = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user")


class RecentTrack(models.Model):
    Songs = models.ForeignKey("Songs", on_delete=models.CASCADE, related_name="songs")
    Recent = models.ForeignKey("Recent", on_delete=models.CASCADE, related_name="recent")


class Favourites(models.Model):
    User = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user")


class FavouriteTrack(models.Model):
    Favourites = models.ForeignKey("Favourites", on_delete=models.CASCADE, related_name="favourites")
    Songs = models.ForeignKey("Songs", on_delete=models.CASCADE, related_name="songs")


class Downloads(models.Model):
    User = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user")


class DownloadTrack(models.Model):
    Downloads = models.ForeignKey("Downloads", on_delete=models.CASCADE, related_name="downloads")
    Songs = models.ForeignKey("Songs", on_delete=models.CASCADE, related_name="songs")


class Podcast(models.Model):
    podcast_name = models.CharField(max_length=255, verbose_name="song_name")
    podcast_url = models.CharField(max_length=255, verbose_name="song_name")


class Video(models.Model):
    VIDEO_CATEGORY = (
        ('HORROR', 'horror'),
        ('COMEDY', 'comedy'),
        ('ACTION', 'action'),
        ('ROMANCE', 'romance'),
        ('ADVENTURE', 'adventure'),
        ('TRAGEDY', 'tragedy'),
        ('SCI-FI', 'sci-fi'),
    )
    video_name = models.CharField(max_length=255, verbose_name="video_name")
    video_date = models.DateTimeField(max_length=255, verbose_name="video_date")
    video_url = models.CharField(max_length=255, verbose_name="video_url")
    video_img_url = models.CharField(max_length=255, verbose_name="video_img_url")


