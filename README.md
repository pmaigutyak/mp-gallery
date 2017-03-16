# MP-Gallery

Django gallery app.

### Installation

Install with pip:

```sh
$ pip install django-mp-gallery
```

### Gallery.photos
Add photos to settings.py:

```
INSTALLED_APPS = [
    'gallery.photos',
]
```

### Gallery.videos
Add videos to settings.py:

```
INSTALLED_APPS = [
    'gallery.videos',
]
```

Run migrations:

```
$ python manage.py migrate
```

### Requirements

App require this packages:

* django-modeltranslation
* django-multiupload
* django-cleanup
* sorl-thumbnail
* awesome-slugify
* django-ordered-model
* django-pure-pagination
