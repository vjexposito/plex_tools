#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plexapi.server import PlexServer, CONFIG
import requests
import re
import os
import urllib.request

"""

Get Movie and TV Show poster and fantart images from Plex.
Based on the work done here: https://github.com/blacktwin/JBOPS/blob/master/utility/plex_api_poster_pull.py

"""

library_name = ['Movies', 'Series']  # Your library names
root_path = 'D:/Plex/'

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


def check_path(path):
    if not os.path.isdir(path):
        os.mkdir(path)


# Check if the root exits or a new one has to be created
check_path(root_path)

# Create paths for Movies and TV Shows inside current directory
movie_path = '{}/Movies'.format(os.path.dirname(root_path))
check_path(movie_path)


show_path = '{}/TV Shows'.format(os.path.dirname(root_path))
check_path(show_path)


def save_file(path, url):
    # Check if file already exists
    if os.path.isfile(path):
        print("ERROR, %s already exist" % path)
    else:
        # Save to directory
        urllib.request.urlretrieve(url, path)


# Get all movies or shows from LIBRARY_NAME
for library in library_name:
    for child in plex.library.section(library).all():
        library_path = ''
        if child.type == 'movie':
            library_path = '{}/{}'.format(movie_path, library)
        elif child.type == 'show':
            library_path = '{}/{}'.format(show_path, library)
        # library_path = '{}/{}'.format(movie_path, library)
        check_path(library_path)
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
        child_path = '{}/{}'.format(library_path, name)
        check_path(child_path)
        poster_path = u'{}/poster.jpg'.format(child_path)
        save_file(poster_path, thumb_url)
        fanart_path = u'{}/fanart.jpg'.format(child_path)
        save_file(fanart_path, fanart_url)
