#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import re
import markdown

AUTHOR = u'Sol Lago'
SITENAME = u'Sol Lago'
# For local development this makes all the links to the homepage work.
# This value needs to be set to production URL in publishconf.py
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Custom Config for Sol Lago
# ==========================

# Enabling serving of static files as recommended here:
# http://docs.getpelican.com/en/3.6.3/content.html#linking-to-static-files
# Adding a favicon:
# http://stackoverflow.com/questions/31270373/how-to-add-a-favicon-to-a-pelican-blog
STATIC_PATHS = [
    'pubs',
    'images',
    'css',
    'js',
    'extra/favicon.ico'
]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

THEME = "themes/twenty"

CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

INDEX_SAVE_AS = "blog.html"

DIRECT_TEMPLATES = ['blog']

# Added plugin
PLUGIN_PATHS = ["../pelican_plugins", ]
PLUGINS = ["pelican-md-metayaml", "assets"]


def sidebar(value):
    if value.startswith('archives') or value.startswith('category'):
        return 'right-sidebar'
    elif value == 'index':
        return 'index'
    else:
        return 'no-sidebar'

p_tag_rgx = re.compile(r"<p>|</p>")


def markdown_strip_p(value):
    '''Removes all p tags from markdown content. '''
    raw_md = markdown.markdown(value)
    return p_tag_rgx.sub('', raw_md)

JINJA_FILTERS = {
    'sidebar': sidebar,
    'markdown': markdown_strip_p
}
