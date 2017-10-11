
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class VideosConfig(AppConfig):
    name = 'gallery.videos'
    verbose_name = _("Videos")


default_app_config = 'gallery.videos.VideosConfig'
