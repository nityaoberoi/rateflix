# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urlparse

from django.conf import settings
from libthumbor import CryptoURL

import logging
logger = logging.getLogger()


def remove_url_scheme(url):
    """
    >>> remove_url_scheme('http://www.yipit.com')
    u'www.yipit.com'
    >>> remove_url_scheme('http://a.yipitcdn.com/blah/foo/biz')
    u'a.yipitcdn.com/blah/foo/biz'
    >>> remove_url_scheme('/media/image.jpg')
    u'media/image.jpg'
    """
    parts = list(urlparse.urlsplit(url))
    parts[0] = ''  # removing scheme
    return urlparse.urlunsplit(parts).lstrip('/')


def thumb(img, **kwargs):
    '''
        returns a thumbor url for 'img' with **kwargs as thumbor options.

        Positional arguments:
        img -- can be a string representing the image path or any object with a url property.

        Keyword arguments:
        For the complete list of thumbor options
        https://github.com/globocom/thumbor/wiki/Usage
        and the actual implementation for the url generation
        https://github.com/heynemann/libthumbor/blob/master/libthumbor/url.py
    '''
    # url is DNS sharded url
    try:
        url = img.url
    except ValueError:
        # When trying to access the url of an image object when
        # the image does not exist, a ValueError is raised
        logger.exception("No file for object (%s) in thumbor", img.instance)
        return ''
    except AttributeError:
        # If it's an attribute error, assume it's a string already
        url = img

    if settings.THUMBOR_BASE_URL:
        # If THUMBOR_BASE_URL is explicity set, use that
        base = settings.THUMBOR_BASE_URL
    else:
        # otherwise assume that thumbor is setup behind the same
        # CDN behind the `thumbor` namespace.
        scheme, netloc = urlparse.urlsplit(url)[:2]
        base = '{}://{}/thumbor'.format(scheme, netloc)

    url = remove_url_scheme(url)

    # just for code clarity
    thumbor_kwargs = kwargs

    if 'fit_in' not in thumbor_kwargs:
        thumbor_kwargs['fit_in'] = True

    # normalizes url to make it work localy
    if settings.LOCAL:
        thumbor_kwargs['unsafe'] = True

        # strips 'media/' from the start of the url
        if url.startswith('media/'):
            url = url[len('media/'):]

        url = '{}/{}'.format(settings.AWS_S3_CUSTOM_DOMAIN, url)

    thumbor_kwargs['image_url'] = url

    crypto = CryptoURL(key=settings.THUMBOR_KEY)
    path = crypto.generate(**thumbor_kwargs).lstrip('/')

    return '{}/{}'.format(base, path)
