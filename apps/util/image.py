#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
import Image
from StringIO import StringIO
import os

from django.core.files.base import ContentFile
from django.db.models import ImageField
from django.db.models.fields.files import ImageFieldFile

import logging
logger = logging.getLogger('reader')


class JPEGImageFieldFile(ImageFieldFile):

    def save(self, name, content, save=True):

        if content:
            image = Image.open(content)
            if image.mode not in ('L', 'RGB'):
                image = image.convert("RGB")
            buf = StringIO()
            image.save(buf, format="JPEG")
            new_content_str = buf.getvalue()
            new_content = ContentFile(new_content_str)
        else:
            new_content = None
        old_name = os.path.splitext(name)[0]
        name = "%s%s" % (old_name, '.jpg')
        return super(JPEGImageFieldFile, self).save(name, new_content, save)


class JPEGImageField(ImageField):
    """
    ImageField that converts all images to JPEG on save.
    """
    attr_class = JPEGImageFieldFile


class ImageProcessor(object):
    """This class is just an abstraction of the steps involved in
    grabbing a product image.

    Usage is easy as 1, 2, 3 (\o/ yay)

    >>> model = SomeModelThatHasAnImage()
    >>> assert hasattr(model, 'image')
    >>>
    >>> processor = ImageProcessor(model)
    >>> processor.process()
    """

    @classmethod
    def process(self, field, url):
        """this is the ONLY entry point to the image processor.
        This is how it works:

        1. It gets the image url from the model instance
        2. The URL is empty ? Bail out and log to sentry
        3. If the URL exists then it will fetch the image data (__fetch method)
        4. An InMemoryUploadedFile is created with the bytes of
            the image (__fetch method)
        5. The image is persisted in the disk (__persist)
        """
        if not url:
            return

        return self.__fetch(field, url)

    @classmethod
    def __fetch(self, field, url):
        res = requests.get(url)
        if not res.ok:
            return
        try:
            return ContentFile(res.content)
            # return InMemoryUploadedFile(
            #     file=StringIO(res.content),
            #     field_name=field,
            #     name=hashlib.md5(res.content).hexdigest(),
            #     content_type=res.headers.get('content-type'),
            #     size=res.headers.get('content-length'),
            #     charset=None
            # )
        except IOError as e:
            logger.warning('Could not get image at %s. Reason: %s',
                url, unicode(e))

