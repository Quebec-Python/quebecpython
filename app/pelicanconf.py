#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Les organisateurs de Québec-Python'
SITENAME = u'Québec-Python'
SITEURL = ''

TIMEZONE = 'America/Montreal'

THEME = "themes/quebecpython"

IGNORE_FILES = (
    "*.less",
    "Grunt*",
    "package.json",
    ".*",
    "node_modules/*"
)

PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (
    ('Liste de diffusion', 'https://groups.google.com/forum/?hl=fr#!forum/quebec-python', "qcpy-mailing-list"),
    ('Groupe Facebook', 'https://www.facebook.com/groups/quebecpython/', "qcpy-facebook"),
    ('Twitter' , 'https://twitter.com/quebecpy', "qcpy-twitter"),
    ('Trello' , 'https://trello.com/b/ACTUjx3z/quebec-python', "qcpy-trello"),
    ('Github' , 'https://github.com/Quebec-Python', "qcpy-github"),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
