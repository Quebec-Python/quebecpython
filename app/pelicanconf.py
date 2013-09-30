#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bernard Chhun'
SITENAME = u'Québec-Python'
SITEURL = ''

TIMEZONE = 'America/Montreal'

THEME = "themes/quebecpython"

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (
    ('Liste de diffusion', 'https://groups.google.com/forum/?hl=fr#!forum/quebec-python'),
    ('Groupe Facebook', 'https://www.facebook.com/groups/quebecpython/'),
    ('Twitter' , 'https://twitter.com/quebecpy'),
    ('Trello' , 'https://trello.com/b/ACTUjx3z/quebec-python'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
