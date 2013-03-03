# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from util.thumborz import thumb

register = template.Library()


@register.simple_tag
def thumbor_url(image_url, **kwargs):
    return thumb(image_url, **kwargs)
