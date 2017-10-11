
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PhotosConfig(AppConfig):
    name = 'gallery.photos'
    verbose_name = _("Photos")


default_app_config = 'gallery.photos.PhotosConfig'
