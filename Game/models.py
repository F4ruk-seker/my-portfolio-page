from django.db import models
from Game.core import UrlSharing, Content
from urllib.parse import urlparse


class GameVideoModel(models.Model):
    title = models.TextField(default=None, null=True)
    description = models.TextField()
    video_length = models.IntegerField()
    url = models.URLField(default=None, null=True, blank=True)
    thumbnail = models.URLField(default=None, null=True, blank=True)
    # sub_thumbnail


class GameInfoModel(models.Model):
    name = models.TextField(default=None, null=True)
    game_type = models.ManyToManyField('GameTypeModels')


class GameTypeModels(models.Model):
    tag = models.TextField(default=None, null=True)
    icon = models.TextField(default=None, null=True)


class MusicInfoModel(models.Model):
    title = models.TextField(default=None, null=True, blank=True)
    description = models.TextField(default=None, null=True, blank=True)
    image = models.URLField(default=None, null=True, blank=True)
    url = models.URLField(default=None, null=True, blank=True)
    length = models.IntegerField(default=None, null=True, blank=True)

    def save(self, *args, **kwargs):
        source = UrlSharing(self.url)
        content = source.get_content()
        if self.title is None or self.title == '':
            self.title = content.get('title', None)
        if self.description is None or self.description == '':
            self.description = content.get('description', None)
        if self.image is None:
            self.image = content.get('image', None)

        super().save(*args, **kwargs)

    @property
    def is_spotify_url(self):
        try:
            parsed_url = urlparse(self.url)
            return parsed_url.hostname in ['spotify.com', 'open.spotify.com']
        except:
            pass

    def __str__(self):
        platform = 'Spotify' if self.is_spotify_url else 'YouTube'
        return f'Music {self.title} | {platform}'


class Game(models.Model):
    video = models.ForeignKey('GameVideoModel', default=None, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField('GameTypeModels')
    info = models.ForeignKey('GameInfoModel', default=None, null=True, on_delete=models.CASCADE)
    songs = models.ManyToManyField('MusicInfoModel')
    pin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
