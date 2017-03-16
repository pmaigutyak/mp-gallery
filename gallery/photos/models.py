
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from slugify import slugify_url
from ordered_model.models import OrderedModel


def get_album_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    return '%s/%s.%s' % ('album_logos', instance.slug, ext)


def get_photo_upload_path(instance, filename):
    return '%s/%s/%s' % ('album_photos', instance.album.slug, filename)


class Album(OrderedModel):

    name = models.CharField(_('Name'), max_length=255, blank=False)

    logo = models.ImageField(
        _('Logo'), blank=True, upload_to=get_album_upload_path)

    description = models.CharField(
        _('Description'), max_length=255, blank=True)

    objects = models.Manager()

    @property
    def slug(self):
        return slugify_url(self.name, separator='_')

    def get_absolute_url(self):
        return reverse('photos:photo-list', kwargs={
            'album_slug': self.slug,
            'album_pk': self.pk
        })

    def __unicode__(self):
        return self.name

    class Meta(OrderedModel.Meta):
        verbose_name = _('Album')
        verbose_name_plural = _('Albums')


class Photo(OrderedModel):

    album = models.ForeignKey(
        Album, verbose_name=_('Album'), related_name='photos')

    file = models.ImageField(
        _('File'), blank=False, upload_to=get_photo_upload_path)

    order_with_respect_to = 'album'

    class Meta(OrderedModel.Meta):
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')
