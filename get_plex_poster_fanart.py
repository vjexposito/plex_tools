#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plexapi.server import PlexServer, CONFIG
import requests
import re
import os
import urllib.request

library_name = ['Movies', 'TV Shows']  # Your library names

PLEX_URL = ''
PLEX_TOKEN = ''
PLEX_URL = CONFIG.data['auth'].get('server_baseurl', PLEX_URL)
PLEX_TOKEN = CONFIG.data['auth'].get('server_token', PLEX_TOKEN)

sess = requests.Session()
# Ignore verifying the SSL certificate
sess.verify = False  # '/path/to/certfile'
# If verify is set to a path to a directory,
# the directory must have been processed using the c_rehash utility supplied
# with OpenSSL.
if sess.verify is False:
    # Disable the warning that the request is insecure, we know that...
    import urllib3

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

plex = PlexServer(PLEX_URL, PLEX_TOKEN, session=sess)

# Create paths for Movies and TV Shows inside current directory
movie_path = '{}/Movies'.format(os.path.dirname(__file__))
if not os.path.isdir(movie_path):
    os.mkdir(movie_path)

show_path = '{}/TV Shows'.format(os.path.dirname(__file__))
if not os.path.isdir(show_path):
    os.mkdir(show_path)


def savefile(path, url):
    # Check if file already exists
    if os.path.isfile(path):
        print("ERROR, %s already exist" % path)
    else:
        # Save to directory
        urllib.request.urlretrieve(url, path)


# Get all movies or shows from LIBRARY_NAME
for library in library_name:
    for child in plex.library.section(library).all():
        library_path = '{}/{}'.format(movie_path, library)
        if not os.path.isdir(library_path):
            os.mkdir(library_path)
        # Clean names of special characters
        name = re.sub('\W+', ' ', child.title)
        # Add (year) to name
        name = '{} ({})'.format(name, child.year)
        print(name)
        # Pull URL for poster
        thumb_url = '{}{}?X-Plex-Token={}'.format(PLEX_URL, child.thumb, PLEX_TOKEN)
        print(thumb_url)
        # Pull URL for fanart
        fanart_url = '{}{}?X-Plex-Token={}'.format(PLEX_URL, child.art, PLEX_TOKEN)
        print(fanart_url)
        # Select path based on media_type
        if child.type == 'movie':
            child_path = '{}/{}'.format(library_path, name)
            if not os.path.isdir(child_path):
                os.mkdir(child_path)
            poster_path = u'{}/poster.jpg'.format(child_path)
            savefile(poster_path, thumb_url)
            fanart_path = u'{}/fanart.jpg'.format(child_path)
            savefile(fanart_path, fanart_url)
        elif child.type == 'show':
            image_path = u'{}/{}.jpg'.format(show_path, name)
            savefile(image_path)
        # Check if file already exists
        # if os.path.isfile(image_path):
        #    print("ERROR, %s already exist" % image_path)
        # else:
        # Save to directory
        #    urllib.request.urlretrieve(thumb_url, image_path)
