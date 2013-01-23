from django.contrib import admin

from rateflix.models import (
    WatchPlatform,
    Movie,
    Genre
)


class WatchPlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_year')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(WatchPlatform, WatchPlatformAdmin)
