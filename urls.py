from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

from rateflix.views import LandingView, AutocompleteView

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', LandingView.as_view(), name='home'),
    url(r'^ajax/autocomplete/$', AutocompleteView.as_view(), name='home'),
)

if settings.LOCAL:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
