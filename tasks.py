import os
import shlex
import shutil
import sys

from invoke import task
from invoke.main import program
from pelican import main as pelican_main
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

OPEN_BROWSER_ON_SERVE = True
BASE_SETTINGS_FILE = "pelicanconf.py"
PUBLISH_SETTINGS_FILE = "publishconf.py"

SETTINGS = {**DEFAULT_CONFIG, **get_settings_from_file(BASE_SETTINGS_FILE)}



@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(SETTINGS["OUTPUT_PATH"]):
        shutil.rmtree(SETTINGS["OUTPUT_PATH"])
        os.makedirs(SETTINGS["OUTPUT_PATH"])


@task
def build(c):
    """Build local version of site"""
    pelican_run(f"-s {BASE_SETTINGS_FILE}")


@task
def rebuild(c):
    """`build` with the delete switch"""
    pelican_run(f"-d -s {BASE_SETTINGS_FILE}")


@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    pelican_run(f"-r -s {BASE_SETTINGS_FILE}")


@task
def serve(c, host="localhost", port=8000):
    """Serve site at http://$HOST:$PORT/ (default is localhost:8000)"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        SETTINGS["OUTPUT_PATH"],
        (host, port),
        ComplexHTTPRequestHandler,
    )

    if OPEN_BROWSER_ON_SERVE:
        # Open site in default browser
        import webbrowser

        webbrowser.open(f"http://{host}:{port}")

    sys.stderr.write(f"Serving at {host}:{port} ...\n")
    server.serve_forever()


@task
def reserve(c):
    """`build`, then `serve`"""
    build(c)
    serve(c)


@task
def preview(c):
    """Build production version of site."""
    pelican_run(f"-s {PUBLISH_SETTINGS_FILE}")


@task
def live(c, host="localhost", port=8000):
    """Automatically reload browser tab upon file modification."""
    from livereload import Server

    build(c)
    server = Server()
    theme_path = SETTINGS["THEME"]
    watched_globs = [BASE_SETTINGS_FILE, f"{theme_path}/templates/**/*.html"]

    for path in SETTINGS["PLUGIN_PATHS"]:
        watched_globs.append(f"{path}/**")

    # Watch for chagnes in content folder
    watched_globs.append(f"{SETTINGS['PATH']}/**")

    # Watch CSS changes
    watched_globs.append("styles.css")

    for glob in watched_globs:
        server.watch(glob, lambda: build(c))

    if OPEN_BROWSER_ON_SERVE:
        # Open site in default browser
        import webbrowser

        webbrowser.open(f"http://{host}:{port}")

    server.serve(host=host, port=port, root=SETTINGS["OUTPUT_PATH"])


def pelican_run(cmd):
    cmd += " " + program.core.remainder  # allows to pass-through args to pelican
    pelican_main(shlex.split(cmd))
