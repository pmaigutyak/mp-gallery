
import gallery.photos.translation

from django.contrib import admin
from django import forms
from django.utils.translation import ugettext as _

from multiupload.fields import MultiFileField
from ordered_model.admin import OrderedModelAdmin
from sorl.thumbnail import get_thumbnail
from modeltranslation.admin import TranslationAdmin

from gallery.photos.models import Photo, Album


class AlbumsAdmin(OrderedModelAdmin, TranslationAdmin):

    list_display = ('name', 'move_up_down_links', )


class UploadPhotosAdminForm(forms.ModelForm):

    album = forms.ModelChoiceField(
        label=_("Album"), required=True, queryset=Album.objects.all())

    images = MultiFileField(label=_('Images'), max_num=100, min_num=1)

    class Meta:
        model = Photo
        exclude = ['order', 'file']


class PhotosAdmin(OrderedModelAdmin):

    list_display = ['file', 'preview', 'album', 'move_up_down_links']

    list_filter = ('album', )

    def preview(self, item):
        try:
            preview = get_thumbnail(item.logo, '100x100', crop='center', quality=99)
            return '<img src="%s" style="width: 60px;" />' % preview.url
        except Exception as e:
            return '--------'
    preview.allow_tags = True

    def save_model(self, request, obj, form, change):

        files = request.FILES.getlist('images')
        data = form.cleaned_data
        for file in files:
            self.model.objects.create(
                album=data['album'],
                file=file
            ).top()

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            return UploadPhotosAdminForm
        else:
            return super(PhotosAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(Album, AlbumsAdmin)
admin.site.register(Photo, PhotosAdmin)
