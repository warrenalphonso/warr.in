# Publish settings file. It overrides pelicanconf.py
import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# Basic settings
DELETE_OUTPUT_DIRECTORY = False
# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://warr.in"

# URL settings
RELATIVE_URLS = False
