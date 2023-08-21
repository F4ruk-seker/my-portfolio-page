from django.db import models
from Game.core import UrlSharing, Content
from urllib.parse import urlparse
import uuid


class GameVideoModel(models.Model):
    title = models.TextField(default=None, null=True)
    description = models.TextField(default=None, null=True, blank=True)
    video_length = models.PositiveBigIntegerField(default=1, null=True, blank=True)  # django Issue
    url = models.URLField(default=None, null=True, blank=True)
    thumbnail = models.URLField(default=None, null=True, blank=True)
    # sub_thumbnail

    def is_url_in_host_list(self, *host_name_list):
        try:
            parsed_url = urlparse(self.url)
            return parsed_url.hostname in host_name_list
        except:
            pass

    def save(self, *args, **kwargs):
        youtube_embed_host = 'https://www.youtube.com/embed'
        if self.is_url_in_host_list('youtube.com', 'www.youtube.com', 'youtu.be', 'www.youtu.be'):
            parsed_url = urlparse(self.url)
            if not parsed_url.path.startswith('/embed'):
                if len(parsed_url.query) > 0:
                    self.url = youtube_embed_host + parsed_url.query.replace('v=', '/')
                else:
                    self.url = youtube_embed_host + parsed_url.path
        super().save(*args, **kwargs)


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
    length = models.PositiveBigIntegerField(default=1, null=True, blank=True)

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
    def compatible_name(self):
        return self.title if len(self.title) < 27 else f'{self.title[:26]} ...'

    @property
    def is_spotify_url(self):
        return self.is_this_url('spotify.com', 'open.spotify.com')

    def is_this_url(self, *host_name_list):
        try:
            parsed_url = urlparse(self.url)
            return parsed_url.hostname in host_name_list
        except:
            pass

    def __str__(self):
        platform = 'Spotify' if self.is_spotify_url else 'YouTube'
        return f'Music {self.title} | {platform}'


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video = models.ForeignKey('GameVideoModel', default=None, null=True, on_delete=models.CASCADE,
                              verbose_name='game_video')
    tags = models.ManyToManyField('GameTypeModels')
    info = models.ForeignKey('GameInfoModel', default=None, null=True, on_delete=models.CASCADE,
                             verbose_name='game_info')
    songs = models.ManyToManyField('MusicInfoModel')
    pin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    view = models.ManyToManyField('base.ViewModel', blank=True, default=None, editable=False)
