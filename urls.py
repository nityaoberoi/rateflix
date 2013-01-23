from django.conf.urls import patterns, url, include

from django.contrib import admin
admin.autodiscover()

from rateflix.views import LandingView

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', LandingView.as_view(), name='home'),
)
