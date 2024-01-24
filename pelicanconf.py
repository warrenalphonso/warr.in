# Base settings file: https://docs.getpelican.com/en/latest/settings.html
from markdown_extensions import MathJaxExtension, PriceContextExtension

# Basic settings
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["blog"]
PATH = "content"
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["colorize"]
SITENAME = "warr.in"
SITEURL = ""
STATIC_PATHS = ["favicon.ico", "pygment-lovelace.css", "CPILFESL.csv", "images"]
MARKDOWN = {
    "extensions": [
        "markdown.extensions.codehilite",  # Syntax highlighting
        "markdown.extensions.extra",
        "markdown.extensions.meta",
        "pymdownx.tilde",
        MathJaxExtension(),
        PriceContextExtension(),
    ],
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
    },
}

# URL settings
ARTICLE_URL = "blog/{path_no_ext}/"
ARTICLE_SAVE_AS = "blog/{path_no_ext}/index.html"
ARCHIVES_SAVE_AS = "blog/index.html"
CATEGORY_URL = ""
CATEGORY_SAVE_AS = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""

# Time and Date settings
TIMEZONE = "America/Los_Angeles"

# Template pages
DIRECT_TEMPLATES = ["archives"]

# Metadata settings
# Regex to turn full path into filename without extension
# The ?P<path_no_ext> is a Python group name, so we can extract it with .group("path_no_ext")
PATH_METADATA = r".*/(?P<path_no_ext>.*)\..*"

# Feed settings
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Pagination settings
DEFAULT_PAGINATION = 10

# Translations settings
DEFAULT_LANG = "en"

# Themes
THEME = "./theme"
