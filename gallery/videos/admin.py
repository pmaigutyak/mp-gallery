
import gallery.videos.translation

from django.contrib import admin

from ordered_model.admin import OrderedModelAdmin
from sorl.thumbnail import get_thumbnail
from modeltranslation.admin import TranslationAdmin

from gallery.videos.models import Video, Album


class AlbumsAdmin(OrderedModelAdmin, TranslationAdmin):

    list_display = ('name', 'move_up_down_links', )


class VideoAdmin(OrderedModelAdmin):

    list_display = ['name', 'preview', 'album', 'move_up_down_links']

    list_filter = ('album', )

    def preview(self, item):
        try:
            preview = get_thumbnail(item.logo, '100x100', crop='center', quality=99)
            return '<img src="%s" style="width: 60px;" />' % preview.url
        except Exception as e:
            return '--------'

    preview.allow_tags = True


admin.site.register(Album, AlbumsAdmin)
admin.site.register(Video, VideoAdmin)
