#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yuki Kobayashi'
SITENAME = u'Self introduction'
SITEURL = ''
SITELOGO = 'http://graph.facebook.com/884948354947695/picture?type=large'
SITETITLE = AUTHOR
SITESUBTITLE = 'Engineer & Product Manager'

SITEDESCRIPTION = u'%s\'s Self Introduction' % AUTHOR

PATH = 'content'

TIMEZONE = 'Japan'

DEFAULT_LANG = u'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('github', 'https://github.com/akerue'),
          ('facebook', 'https://www.facebook.com/yuuki.kobayashi.399'),
          ('twitter', 'https://twitter.com/Robbykunsan'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = './Flex-master'

COPYRIGHT_YEAR = 2016


FAVICON = 'favicon.ico'
FAVICON_TYPE = 'image/vnd.microsoft.icon'

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/' + FAVICON: {'path': FAVICON},
}
