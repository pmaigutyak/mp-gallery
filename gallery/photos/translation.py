
from modeltranslation.translator import translator, TranslationOptions

from gallery.photos.models import Album


class AlbumTranslationOptions(TranslationOptions):
    fields = ('name', 'description', )


translator.register(Album, AlbumTranslationOptions)
