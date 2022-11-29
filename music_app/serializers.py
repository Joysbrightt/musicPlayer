# from rest_frameworks

from rest_framework import serializers
from .models import User, Songs, Playlist, PlaylistTrack, DownloadTrack, Downloads, RecentTrack, Recent, Podcast, Video, FavouriteTrack, Favourites


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_name', 'email', 'password']


class PlaylistSerializer(serializers.ModelSerializer):
    # Playlist = serializers.HyperlinkedIdentityField(
    #     queryset=Playlist.objects.all(),
    #     view_name="music_app: Songs_detail"
    # )
    class Meta:
        model = Playlist
        fields = ['playlist_name', 'user']


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ['song_name', 'song_url', 'song_date', 'song_artist']


class PlaylistTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model= PlaylistTrack
        fields = ['playlist', 'songs_id']


class RecentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recent
        fields = [
            'user_id'
        ]


class RecentTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recent
        fields = ['songs', 'recent_id']


class FavouritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourites
        fields = ['user_id']


class FavouriteTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteTrack
        fields = ['favourites_id', 'song_id']


class DownloadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Downloads
        fields = ["user_id"]


class DownloadTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadTrack
        fields = ['downloads_id', 'song-id']


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ['podcast_name', 'podcast']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['video_name', 'video_date', 'video_url', 'video_img_url', 'video_category']
