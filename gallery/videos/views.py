
from django.shortcuts import render, get_object_or_404

from pure_pagination import Paginator

from gallery.videos.models import Album


def album_list(request):

    albums = Album.objects.all()

    return render(request, 'gallery/album_list.html', {'albums': albums})


def video_list(request, album_slug, album_pk):

    album = get_object_or_404(Album, pk=album_pk)

    paginator = Paginator(album.videos.all(), 20, request=request)

    context = {
        'album': album,
        'videos': paginator.page(request.GET.get('page', 1))
    }

    return render(request, 'gallery/video_list.html', context)


def video_info(request, album_slug, album_pk, video_slug, video_pk):

    album = get_object_or_404(Album, pk=album_pk)

    video = get_object_or_404(album.videos.all(), pk=video_pk)

    context = {
        'album': album,
        'video': video
    }

    return render(request, 'gallery/video_info.html', context)
