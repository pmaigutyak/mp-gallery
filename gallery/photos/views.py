
from django.shortcuts import render, get_object_or_404

from pure_pagination import Paginator

from gallery.photos.models import Album


def album_list(request):

    albums = Album.objects.all()

    return render(request, 'gallery/album_list.html', {'albums': albums})


def photo_list(request, album_slug, album_pk):

    album = get_object_or_404(Album, pk=album_pk)

    paginator = Paginator(album.photos.all(), 20, request=request)

    context = {
        'album': album,
        'photos': paginator.page(request.GET.get('page', 1))
    }

    return render(request, 'gallery/photo_list.html', context)
