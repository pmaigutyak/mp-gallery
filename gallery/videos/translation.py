
from modeltranslation.translator import translator, TranslationOptions

from gallery.videos.models import Album, Video


class AlbumTranslationOptions(TranslationOptions):
    fields = ('name', 'short_description', 'full_description', )


class VideoTranslationOptions(TranslationOptions):
    fields = ('name', 'description', )


translator.register(Album, AlbumTranslationOptions)
translator.register(Video, VideoTranslationOptions)
