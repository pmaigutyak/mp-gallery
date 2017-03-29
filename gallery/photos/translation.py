
from modeltranslation.translator import translator, TranslationOptions

from gallery.photos.models import Album


class AlbumTranslationOptions(TranslationOptions):
    fields = ('name', 'short_description', 'full_description', )


translator.register(Album, AlbumTranslationOptions)
